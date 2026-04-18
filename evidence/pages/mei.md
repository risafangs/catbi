---
title: CatBI
---

```sql events_last_30d 
    select *
    from catdb_new.events
    where date >= current_date - interval '31 days' 
    order by date desc
```

### Logged events, last 30 days
<DataTable data={events_last_30d} />

```sql vomit_data
    select 
        date_trunc('month', date) as month 
        , type
        , count(*) as event_ct

    from catdb_new.events
    where type in ('vomit', 'hairball')
    group by all
```

<BarChart 
    data={vomit_data}
    x=month
    y=event_ct
    yMax = 18  
    series=type
    title="Vomit Trends"
    subtitle="Type of Vomit by Month"
    colorPalette={[
        '#D98FF5',
        '#5037EE'
    ]}>
    
    <ReferenceArea xMin='2024-04-01' xMax='2024-04-30' label='Fostered Aggie' />
    <ReferenceArea xMin='2024-08-01' xMax='2024-09-30' label='Fostered Fawn' />

</BarChart>


```sql vomit_time_of_day
    select
        time_of_day
        , type
        , count(*) as count
 
    from catdb_new.events
    where type in ('vomit', 'hairball')
    group by 1, 2
```

<BarChart 
    data={vomit_time_of_day}
    x=time_of_day
    y=count
    series=type
    swapXY=true
/>

```sql weight
    select
        date
        , value as weight

    from health_stats
    where measurement_type = 'weight'
```

<LineChart
    data={weight}
    x=date
    y=weight
    labels=true
    title="Measured Weight (lbs) Over Time">
    

</LineChart>

