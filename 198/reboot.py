from dateutil.parser import parse

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    boots = []
    for line in reboots.splitlines():
        try:
            line = line.split('~')
            boot_time = line[1].strip()
            boots.append(boot_time)
        except IndexError:
            continue

    boots = [parse(boot) for boot in boots]
    time_diff = [(boots[x] - boots[x+1]).days
                 for x in range(len(boots)) if x != len(boots) - 1
                 ]
    return max(zip(time_diff, [boot.strftime('%Y-%m-%d') for boot in boots]))
