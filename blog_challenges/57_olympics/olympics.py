import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import plotly.graph_objects as go
import plotly.express as px

summer = pd.read_csv('summer.csv')


def most_medals_by_athlete(gender: str):
    if gender not in ['Men', 'Women']:
        raise ValueError('gender must be Men or Women')

    medal_count = summer.groupby(['Athlete', 'Gender'])['Medal'].count()
    medal_count = medal_count.sort_values(ascending=False)

    if gender == 'Men':
        # get group of Men
        medal_count = list(medal_count.groupby('Gender'))[0][1]
        # get name of Athlete with most medals as Last, First
        last_name, first_name = medal_count.index[0][0].title().split(',')
        # return name of Athlete as First Last
        return f'{first_name.strip()} {last_name}'
    elif gender == 'Women':
        # get group of Women
        medal_count = list(medal_count.groupby('Gender'))[1][1]
        # get name of Athlete with most medals as Last, First
        last_name, first_name = medal_count.index[0][0].title().split(',')
        # return name of Athlete as First Last
        return f'{first_name.strip()} {last_name}'


def most_medals_by_country(gender: str):
    if gender not in ['Men', 'Women']:
        raise ValueError('gender must be Men or Women')

    medal_count = summer.query(
        f'Gender == "{gender}"').groupby(
            ['Country'])['Medal'].count().sort_values(ascending=False)
    return medal_count.head(10)


def top_10_bar_plot(gender: str):
    if gender not in ['Men', 'Women']:
        raise ValueError('gender must be Men or Women')

    colors = []
    if gender == 'Men':
        colors = ['#F53939', '#F53939', '#0000CC', '#0000CC', '#16AF3A',
                  '#FFFF66', '#000000', '#16AF3A', '#0000CC', '#F53939'
                  ]
    if gender == 'Women':
        colors = ['red', 'red', 'red', 'green', 'black', 'yellow',
                  'red', 'orange', 'yellow', 'blue'
                  ]

    top_10 = most_medals_by_country(gender)
    top_10.plot(kind='bar',
                y='Medal',
                ylabel='Medals',
                title=f'Olympic Medals by Country 1896-2012 ({gender})',
                rot=0,
                color=colors,
                )
    plt.show()


def most_medals_by_sport(df=summer):
    sports = summer.groupby('Sport')['Medal'].count().sort_values(
        ascending=False).head(10)

    sports.plot(kind='bar',
                y='Medal',
                ylabel='Medals',
                rot=45,
                colormap=cm.Accent,
                )
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.title(('Olympic Medals Awarded by Sport (Top 10) '
               'from 1896-2012 - Summer'),
              size='medium',
              )
    plt.savefig('images/medals_by_sport.png')


def medals_by_country_plotly():
    medal_count = summer.groupby(
            'Country', as_index=False)['Medal'].count().sort_values(
                by='Medal', ascending=False)
    layout = dict(title=('Olympic Medals Awarded by Country '
                         '1896-2012 - Summer Games'),
                  geo=dict(countrycolor='#444444', showcountries=True,
                           showocean=True,
                           projection={'type': 'natural earth'}))
    data = go.Choropleth(locations=medal_count['Country'],
                         locationmode='ISO-3',
                         z=medal_count['Medal'],
                         colorscale=px.colors.sequential.YlGn)
    fig = go.Figure(data=data, layout=layout)
    fig.show()


def region_scopes(region: str):
    # Pass to geo for region selection on map.
    return dict(countrycolor='#444444',
                showcountries=True,
                oceancolor='deepskyblue',
                showocean=True,
                lakecolor='deepskyblue',
                showlakes=True,
                projection={'type': 'natural earth'},
                scope=region,
                )


def cycling_medals_by_country_plotly():
    cycling = summer.query('Sport == "Cycling"').groupby(
                ['Country'], as_index=False)['Medal'].count(
                    ).sort_values(by='Medal', ascending=False)

    # FIX COUNTRY CODES FOR ISO-3
    cycling['Country'] = cycling['Country'].replace(
        ['GER', 'NED', 'DEN', 'SUI', 'RSA', 'GRE', 'LAT', 'POR', 'URU'],
        ['DEU', 'NLD', 'DNK', 'CHE', 'ZAF', 'GRC', 'LVA', 'PRT', 'URY']
        )

    layout = dict(title=dict(text=('Olympic Cycling Medals Awarded by Country '
                             '1896-2012'),
                             x=0.5,
                             ),
                  geo=region_scopes('world')
                  )
    data = go.Choropleth(locations=cycling['Country'],
                         locationmode='ISO-3',
                         z=cycling['Medal'],
                         colorscale=px.colors.sequential.Oryel)
    fig = go.Figure(data=data, layout=layout)

    # Add Region Selector
    fig.update_layout(
        updatemenus=[
            dict(buttons=list([
                dict(label='World',
                     method='relayout',
                     args=['geo', region_scopes('world')]),
                dict(label='Africa',
                     method='relayout',
                     args=['geo', region_scopes('africa')]),
                dict(label='Asia',
                     method='relayout',
                     args=['geo', region_scopes('asia')]),
                dict(label='Europe',
                     method='relayout',
                     args=['geo', region_scopes('europe')]),
                dict(label='North America',
                     method='relayout',
                     args=['geo', region_scopes('north america')]),
                dict(label='South America',
                     method='relayout',
                     args=['geo', region_scopes('south america')])
            ]),
             x=0.15,
             y=0.95,
            )
        ]
    )

    # Add annotation and place dropdown
    fig.update_layout(
        annotations=[
            dict(text='Region:',
                 x=0.051,
                 y=1,
                 showarrow=False)
        ]
    )

    # fig.show()
    fig.write_html('images/cycling_medals.html')
