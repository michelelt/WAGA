import pandas as pd

class Analytics:
    def __init__(self, df, dpu):
        self.df = df
        self.df['date'] = pd.to_datetime(df['date'])
        self.df['Hour'] = self.df.date.dt.hour
        self.df['Month'] = self.df.date.dt.month
        self.df['Year'] = self.df.date.dt.year
        self.df['dow'] = self.df.date.dt.dayofweek
        self.df['date_only'] = self.df.date.dt.date


        self.dpu = dpu

    def message_per_user(self, norm=False):
        grouped = self.df.groupby('user').count()['mex'].sort_values()
        if norm == False:
            return grouped
        else:
            return grouped.div(self.dpu['days']).sort_values()

    def message_per_label(self, label, df=None, mean=True):
        if df != None: target_df = df
        else: target_df = self.df

        target_df = target_df.reset_index()
        target_df = target_df.rename(columns={'index':'Counter'})

        if mean== False:
            tot = target_df.groupby(label).count()['Counter'].sort_index()
            we = target_df[target_df.dow.isin([5,6])]\
                .groupby(label).count()['Counter'].sort_index()
            wd = target_df[~target_df.dow.isin([5,6])]\
                .groupby(label).count()['Counter'].sort_index()
        else:
            tot = target_df.groupby(label).mean()['Counter'].sort_index()
            we = target_df[target_df.dow.isin([5,6])]\
                .groupby(label).mean()['Counter'].sort_index()
            wd = target_df[~target_df.dow.isin([5,6])]\
                .groupby(label).mean()['Counter'].sort_index()

        return dict(tot=tot, we=we, wd=wd)

    def mex_per_day_by_user(self, bench_mark, users):
        date_min = self.df.date.dt.date.min()
        date_max = self.df.date.dt.date.max()

        mpd_by_user = pd.DataFrame()
        mpd_by_user['date'] = pd.date_range(start=date_min, end=date_max)
        mpd_by_user['date'] = pd.to_datetime( mpd_by_user['date'])
        mpd_by_user['date'] = mpd_by_user.date.dt.date


        for user in users:
            us_per_day = self.df[self.df.user == user]
            us_per_day = us_per_day.groupby('date_only').count()['message'].to_frame()
            mpd_by_user = mpd_by_user.merge(us_per_day, left_on='date', right_index=True, how='left')
            mpd_by_user = mpd_by_user.rename(columns={'message': '%s' % user})

        mpd_by_user = mpd_by_user.set_index('date')
        return mpd_by_user.fillna(0)


    def temporal_evolution_per_day(self):
        grouped_df = self.df.groupby('date_only').count()
        return grouped_df




