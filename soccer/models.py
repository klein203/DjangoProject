from django.db import models


# Create your models here.
class Nation(models.Model):
    name = models.CharField(name='name', verbose_name=r'国家', max_length=100)
    create_time = models.DateTimeField(name='create_time', verbose_name=r'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(name='update_time', verbose_name=r'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = r'国家'
        verbose_name_plural = verbose_name


class Team(models.Model):
    name = models.CharField(name='name', verbose_name=r'队伍', max_length=100)
    abbr_name = models.CharField(name='abbr_name', verbose_name=r'缩写', max_length=20)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, verbose_name=r'国家')
    create_time = models.DateTimeField(name='create_time', verbose_name=r'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(name='update_time', verbose_name=r'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = r'队伍'
        verbose_name_plural = verbose_name


class League(models.Model):
    name = models.CharField(name='name', verbose_name=r'联赛', max_length=100)
    season = models.CharField(name='season', verbose_name=r'赛季', max_length=20)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, verbose_name=r'国家')
    create_time = models.DateTimeField(name='create_time', verbose_name=r'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(name='update_time', verbose_name=r'更新时间', auto_now=True)

    def __str__(self):
        return '%s %s' % (self.name, self.season)

    class Meta:
        verbose_name = r'联赛'
        verbose_name_plural = verbose_name


class Schedule(models.Model):
    name = models.CharField(name='name', verbose_name=r'赛程', max_length=20)
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name=r'联赛')
    start_date = models.DateField(name='start_date', verbose_name=r'开始日期')
    end_date = models.DateField(name='end_date', verbose_name=r'结束日期')
    create_time = models.DateTimeField(name='create_time', verbose_name=r'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(name='update_time', verbose_name=r'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = r'赛程'
        verbose_name_plural = verbose_name


class Match(models.Model):
    # name = models.CharField(name='name', verbose_name=r'比赛', max_length=100)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='schedule', verbose_name=r'轮次')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team', verbose_name=r'主队')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team', verbose_name=r'客队')
    home_score = models.IntegerField(name='home_score', verbose_name=r'主队得分', null=True, blank=True)
    away_score = models.IntegerField(name='away_score', verbose_name=r'客队得分', null=True, blank=True)
    schedule_date = models.DateField(name='schedule_date', verbose_name=r'预计比赛日期')
    match_date = models.DateField(name='match_date', verbose_name=r'实际比赛日期', null=True, blank=True)
    create_time = models.DateTimeField(name='create_time', verbose_name=r'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(name='update_time', verbose_name=r'更新时间', auto_now=True)

    def __str__(self):
        return '%s vs %s @%s' % (self.home_team, self.away_team, self.schedule_date)

    class Meta:
        verbose_name = r'比赛'
        verbose_name_plural = verbose_name
