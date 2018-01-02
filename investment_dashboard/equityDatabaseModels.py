# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BasketValues(models.Model):
    basket_val_id = models.BigAutoField(primary_key=True)
    basket = models.ForeignKey('Baskets', models.DO_NOTHING)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket_values'


class Baskets(models.Model):
    basket_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_by = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baskets'


class Classification(models.Model):
    classification_id = models.BigAutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    standard = models.TextField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    level_1 = models.TextField(blank=True, null=True)
    level_2 = models.TextField(blank=True, null=True)
    level_3 = models.TextField(blank=True, null=True)
    level_4 = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classification'


class ConferenceCalls(models.Model):
    conf_call_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source', blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    event_title = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conference_calls'


class CsidataStockFactsheet(models.Model):
    csi_number = models.TextField(primary_key=True)
    symbol = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    exchange = models.TextField(blank=True, null=True)
    sub_exchange = models.TextField(blank=True, null=True)
    is_active = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    conversion_factor = models.SmallIntegerField(blank=True, null=True)
    switch_cf_date = models.DateField(blank=True, null=True)
    pre_switch_cf = models.SmallIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csidata_stock_factsheet'


class DailyPrices(models.Model):
    daily_price_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey('DataVendor', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    date = models.DateTimeField()
    open = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    high = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    low = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    close = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    ex_dividend = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    split_ratio = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_prices'


class DataVendor(models.Model):
    data_vendor_id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    support_email = models.TextField(blank=True, null=True)
    api = models.TextField(blank=True, null=True)
    consensus_weight = models.SmallIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_vendor'


class Dividends(models.Model):
    dividend_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source', blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    dividend = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    ex_dividend_date = models.DateTimeField()
    record_date = models.DateTimeField(blank=True, null=True)
    announcement_date = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dividends'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Earnings(models.Model):
    earnings_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source', blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    reported_eps = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    consensus_eps = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'earnings'


class EconomicEvents(models.Model):
    event_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source', blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_for = models.DateTimeField(blank=True, null=True)
    actual = models.TextField(blank=True, null=True)
    briefing_forecast = models.TextField(blank=True, null=True)
    market_expects = models.TextField(blank=True, null=True)
    prior = models.TextField(blank=True, null=True)
    revised_from = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'economic_events'


class Exchanges(models.Model):
    exchange_id = models.SmallIntegerField(primary_key=True)
    symbol = models.TextField(unique=True)
    goog_symbol = models.TextField(blank=True, null=True)
    yahoo_symbol = models.TextField(blank=True, null=True)
    csi_symbol = models.TextField(blank=True, null=True)
    tsid_symbol = models.TextField()
    name = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    time_zone = models.TextField(blank=True, null=True)
    utc_offset = models.FloatField(blank=True, null=True)
    open = models.TimeField(blank=True, null=True)
    close = models.TimeField(blank=True, null=True)
    lunch = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exchanges'


class FinraData(models.Model):
    finra_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    date = models.DateTimeField()
    short_volume = models.IntegerField(blank=True, null=True)
    short_exempt_volume = models.IntegerField(blank=True, null=True)
    total_volume = models.IntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finra_data'


class FundamentalData(models.Model):
    fundamental_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey(DataVendor, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    date = models.DateTimeField()
    field = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fundamental_data'


class Indices(models.Model):
    index_id = models.AutoField(primary_key=True)
    stock_index = models.TextField()
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    as_of_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indices'


class IpoPricings(models.Model):
    ipo_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source', blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    offer_date = models.DateTimeField(blank=True, null=True)
    shares_offered = models.TextField(blank=True, null=True)
    proposed_price = models.TextField(blank=True, null=True)
    initial_price = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipo_pricings'


class MinutePrices(models.Model):
    minute_price_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey(DataVendor, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    date = models.DateTimeField()
    close = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    high = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    low = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    open = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minute_prices'


class OptionChains(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey(DataVendor, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    symbol = models.TextField(blank=True, null=True)
    exchange = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    multiplier = models.SmallIntegerField(blank=True, null=True)
    contract_id = models.BigIntegerField()
    expiry = models.DateField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    strike = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pre_split = models.NullBooleanField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option_chains'


class OptionPrices(models.Model):
    option_prices_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey(DataVendor, models.DO_NOTHING, blank=True, null=True)
    option = models.ForeignKey(OptionChains, models.DO_NOTHING)
    date = models.DateTimeField()
    bid = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bid_size = models.IntegerField(blank=True, null=True)
    ask = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ask_size = models.IntegerField(blank=True, null=True)
    close = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    open_interest = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    imp_volatility = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    delta = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    gamma = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    rho = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    theta = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    vega = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option_prices'


class PortfolioPortfoliotransaction(models.Model):
    datetime = models.DateTimeField()
    equitytype = models.CharField(db_column='equityType', max_length=10)  # Field name made lowercase.
    equityname = models.CharField(db_column='equityName', max_length=30)  # Field name made lowercase.
    units = models.DecimalField(max_digits=20, decimal_places=10)
    currency = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'portfolio_portfoliotransaction'


class QuandlCodes(models.Model):
    q_code_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey(DataVendor, models.DO_NOTHING, db_column='data_vendor')
    data = models.TextField()
    component = models.TextField()
    period = models.TextField(blank=True, null=True)
    symbology_source = models.TextField()
    q_code = models.TextField()
    name = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    frequency = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    page_num = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quandl_codes'


class Splits(models.Model):
    split_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Symbology', models.DO_NOTHING, db_column='source', blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    payable_date = models.DateTimeField(blank=True, null=True)
    ex_date = models.DateTimeField(blank=True, null=True)
    announced_date = models.DateTimeField(blank=True, null=True)
    optionable = models.NullBooleanField()
    ratio = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'splits'


class Symbology(models.Model):
    symbol_id = models.BigIntegerField()
    source = models.TextField()
    source_id = models.TextField()
    type = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'symbology'
        unique_together = (('source', 'source_id'),)


class TickPrices(models.Model):
    tick_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey(DataVendor, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey(Symbology, models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    bid = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    ask = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    last = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    high = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    low = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    close = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    bid_size = models.IntegerField(blank=True, null=True)
    ask_size = models.IntegerField(blank=True, null=True)
    last_size = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tick_prices'


class TickPricesStream(models.Model):
    tick_id = models.BigAutoField(primary_key=True)
    data_vendor = models.ForeignKey(DataVendor, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey(Symbology, models.DO_NOTHING, db_column='source')
    source_id = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tick_prices_stream'
