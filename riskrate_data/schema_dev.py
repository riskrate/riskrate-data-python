import sgqlc.types


schema_dev = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String

class company_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_pkey', 'company_vat_key')


class company_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('address', 'bankruptcy', 'business_interruption', 'founded_date', 'id', 'industry', 'liquidation', 'name', 'restructuring', 'time_created', 'time_updated', 'vat')


class company_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('address', 'bankruptcy', 'business_interruption', 'founded_date', 'id', 'industry', 'liquidation', 'name', 'restructuring', 'time_created', 'time_updated', 'vat')


class customer_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('customer_email_key', 'customer_pkey')


class customer_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('email', 'email_subscription', 'group_id', 'id', 'password_hash', 'status', 'time_created', 'time_updated')


class customer_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('email', 'email_subscription', 'group_id', 'id', 'password_hash', 'status', 'time_created', 'time_updated')


class date(sgqlc.types.Scalar):
    __schema__ = schema_dev


class eb_balance_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('eb_balance_pkey',)


class eb_balance_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'balance_type', 'currency', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')


class eb_balance_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'balance_type', 'currency', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')


class eb_bank_account_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('eb_bank_account_account_uid_key', 'eb_bank_account_identification_hash_key', 'eb_bank_account_pkey')


class eb_bank_account_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('account_uid', 'eb_session_info_id', 'id', 'identification_hash', 'time_created', 'time_updated')


class eb_bank_account_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('account_uid', 'eb_session_info_id', 'id', 'identification_hash', 'time_created', 'time_updated')


class eb_keys_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('eb_keys_pkey',)


class eb_keys_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')


class eb_keys_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')


class eb_session_info_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('eb_session_info_pkey', 'eb_session_info_session_id_key')


class eb_session_info_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')


class eb_session_info_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')


class eb_transaction_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('eb_transaction_pkey',)


class eb_transaction_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')


class eb_transaction_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')


class float8(sgqlc.types.Scalar):
    __schema__ = schema_dev


class forecast_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('forecast_pkey',)


class forecast_event_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('forecast_event_pkey',)


class forecast_event_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'data', 'event_class', 'id', 'time_created', 'time_updated', 'type')


class forecast_event_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'data', 'event_class', 'id', 'time_created', 'time_updated', 'type')


class forecast_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')


class forecast_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')


class group_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('group_pkey',)


class group_relation_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('group_relation_pkey',)


class group_relation_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('primary_id', 'secondary_id')


class group_relation_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('primary_id', 'secondary_id')


class group_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'name', 'time_created', 'time_updated')


class group_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'name', 'time_created', 'time_updated')


class invoice_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('invoice_pkey',)


class invoice_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'provider_status', 'reference_number', 'seller_id', 'source', 'status', 'time_created', 'time_updated', 'type')


class invoice_type_enum_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('invoice_type_enum_pkey',)


class invoice_type_enum_enum(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('FINANCIAL', 'OTHER', 'PURCHASE_INVOICE', 'SALARY', 'SALES_INVOICE')


class invoice_type_enum_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('id',)


class invoice_type_enum_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('id',)


class invoice_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'provider_status', 'reference_number', 'seller_id', 'source', 'status', 'time_created', 'time_updated', 'type')


class netvisor_info_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('netvisor_info_pkey',)


class netvisor_info_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'is_active', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')


class netvisor_info_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'is_active', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')


class order_by(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('asc', 'asc_nulls_first', 'asc_nulls_last', 'desc', 'desc_nulls_first', 'desc_nulls_last')


class payment_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('payment_pkey',)


class payment_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'id', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')


class payment_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('amount', 'id', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')


class procountor_info_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('procountor_info_pkey',)


class procountor_info_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'is_active', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')


class procountor_info_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('company_id', 'id', 'is_active', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')


class role_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('role_name_key', 'role_pkey')


class role_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('description', 'id', 'name', 'time_created', 'time_updated')


class role_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('description', 'id', 'name', 'time_created', 'time_updated')


class roles_customers_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('role_id', 'user_id')


class source_enum_constraint(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('source_enum_pkey',)


class source_enum_enum(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('MANUAL', 'NETVISOR', 'PROCOUNTOR')


class source_enum_select_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('id',)


class source_enum_update_column(sgqlc.types.Enum):
    __schema__ = schema_dev
    __choices__ = ('id',)


class timestamp(sgqlc.types.Scalar):
    __schema__ = schema_dev


class timestamptz(sgqlc.types.Scalar):
    __schema__ = schema_dev



########################################################################
# Input Objects
########################################################################
class Boolean_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(Boolean, graphql_name='_eq')
    _gt = sgqlc.types.Field(Boolean, graphql_name='_gt')
    _gte = sgqlc.types.Field(Boolean, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(Boolean, graphql_name='_lt')
    _lte = sgqlc.types.Field(Boolean, graphql_name='_lte')
    _neq = sgqlc.types.Field(Boolean, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='_nin')


class Int_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(Int, graphql_name='_eq')
    _gt = sgqlc.types.Field(Int, graphql_name='_gt')
    _gte = sgqlc.types.Field(Int, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(Int, graphql_name='_lt')
    _lte = sgqlc.types.Field(Int, graphql_name='_lte')
    _neq = sgqlc.types.Field(Int, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_nin')


class String_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_gt', '_gte', '_ilike', '_in', '_is_null', '_like', '_lt', '_lte', '_neq', '_nilike', '_nin', '_nlike', '_nsimilar', '_similar')
    _eq = sgqlc.types.Field(String, graphql_name='_eq')
    _gt = sgqlc.types.Field(String, graphql_name='_gt')
    _gte = sgqlc.types.Field(String, graphql_name='_gte')
    _ilike = sgqlc.types.Field(String, graphql_name='_ilike')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _like = sgqlc.types.Field(String, graphql_name='_like')
    _lt = sgqlc.types.Field(String, graphql_name='_lt')
    _lte = sgqlc.types.Field(String, graphql_name='_lte')
    _neq = sgqlc.types.Field(String, graphql_name='_neq')
    _nilike = sgqlc.types.Field(String, graphql_name='_nilike')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_nin')
    _nlike = sgqlc.types.Field(String, graphql_name='_nlike')
    _nsimilar = sgqlc.types.Field(String, graphql_name='_nsimilar')
    _similar = sgqlc.types.Field(String, graphql_name='_similar')


class company_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('company_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('company_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('company_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('company_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('company_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('company_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('company_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('company_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('company_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('company_variance_order_by', graphql_name='variance')


class company_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('company_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('company_on_conflict', graphql_name='on_conflict')


class company_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class company_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'address', 'bankruptcy', 'business_interruption', 'eb_session_infos', 'forecast_events', 'forecasts', 'founded_date', 'groups', 'id', 'industry', 'invoices_by_buyer', 'invoices_by_seller', 'liquidation', 'name', 'netvisor_infos', 'procountor_infos', 'restructuring', 'time_created', 'time_updated', 'vat')
    _and = sgqlc.types.Field(sgqlc.types.list_of('company_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('company_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('company_bool_exp'), graphql_name='_or')
    address = sgqlc.types.Field(String_comparison_exp, graphql_name='address')
    bankruptcy = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='bankruptcy')
    business_interruption = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='business_interruption')
    eb_session_infos = sgqlc.types.Field('eb_session_info_bool_exp', graphql_name='eb_session_infos')
    forecast_events = sgqlc.types.Field('forecast_event_bool_exp', graphql_name='forecast_events')
    forecasts = sgqlc.types.Field('forecast_bool_exp', graphql_name='forecasts')
    founded_date = sgqlc.types.Field('date_comparison_exp', graphql_name='founded_date')
    groups = sgqlc.types.Field('group_bool_exp', graphql_name='groups')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    industry = sgqlc.types.Field(String_comparison_exp, graphql_name='industry')
    invoices_by_buyer = sgqlc.types.Field('invoice_bool_exp', graphql_name='invoices_by_buyer')
    invoices_by_seller = sgqlc.types.Field('invoice_bool_exp', graphql_name='invoices_by_seller')
    liquidation = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='liquidation')
    name = sgqlc.types.Field(String_comparison_exp, graphql_name='name')
    netvisor_infos = sgqlc.types.Field('netvisor_info_bool_exp', graphql_name='netvisor_infos')
    procountor_infos = sgqlc.types.Field('procountor_info_bool_exp', graphql_name='procountor_infos')
    restructuring = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='restructuring')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')
    vat = sgqlc.types.Field(String_comparison_exp, graphql_name='vat')


class company_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Int, graphql_name='id')


class company_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('address', 'bankruptcy', 'business_interruption', 'eb_session_infos', 'forecast_events', 'forecasts', 'founded_date', 'groups', 'id', 'industry', 'invoices_by_buyer', 'invoices_by_seller', 'liquidation', 'name', 'netvisor_infos', 'procountor_infos', 'restructuring', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(String, graphql_name='address')
    bankruptcy = sgqlc.types.Field(Boolean, graphql_name='bankruptcy')
    business_interruption = sgqlc.types.Field(Boolean, graphql_name='business_interruption')
    eb_session_infos = sgqlc.types.Field('eb_session_info_arr_rel_insert_input', graphql_name='eb_session_infos')
    forecast_events = sgqlc.types.Field('forecast_event_arr_rel_insert_input', graphql_name='forecast_events')
    forecasts = sgqlc.types.Field('forecast_arr_rel_insert_input', graphql_name='forecasts')
    founded_date = sgqlc.types.Field(date, graphql_name='founded_date')
    groups = sgqlc.types.Field('group_arr_rel_insert_input', graphql_name='groups')
    id = sgqlc.types.Field(Int, graphql_name='id')
    industry = sgqlc.types.Field(String, graphql_name='industry')
    invoices_by_buyer = sgqlc.types.Field('invoice_arr_rel_insert_input', graphql_name='invoices_by_buyer')
    invoices_by_seller = sgqlc.types.Field('invoice_arr_rel_insert_input', graphql_name='invoices_by_seller')
    liquidation = sgqlc.types.Field(Boolean, graphql_name='liquidation')
    name = sgqlc.types.Field(String, graphql_name='name')
    netvisor_infos = sgqlc.types.Field('netvisor_info_arr_rel_insert_input', graphql_name='netvisor_infos')
    procountor_infos = sgqlc.types.Field('procountor_info_arr_rel_insert_input', graphql_name='procountor_infos')
    restructuring = sgqlc.types.Field(Boolean, graphql_name='restructuring')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    vat = sgqlc.types.Field(String, graphql_name='vat')


class company_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('address', 'founded_date', 'id', 'industry', 'name', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(order_by, graphql_name='address')
    founded_date = sgqlc.types.Field(order_by, graphql_name='founded_date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    industry = sgqlc.types.Field(order_by, graphql_name='industry')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    vat = sgqlc.types.Field(order_by, graphql_name='vat')


class company_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('address', 'founded_date', 'id', 'industry', 'name', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(order_by, graphql_name='address')
    founded_date = sgqlc.types.Field(order_by, graphql_name='founded_date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    industry = sgqlc.types.Field(order_by, graphql_name='industry')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    vat = sgqlc.types.Field(order_by, graphql_name='vat')


class company_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(company_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('company_on_conflict', graphql_name='on_conflict')


class company_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(company_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(company_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(company_bool_exp, graphql_name='where')


class company_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('address', 'bankruptcy', 'business_interruption', 'eb_session_infos_aggregate', 'forecast_events_aggregate', 'forecasts_aggregate', 'founded_date', 'groups_aggregate', 'id', 'industry', 'invoices_by_buyer_aggregate', 'invoices_by_seller_aggregate', 'liquidation', 'name', 'netvisor_infos_aggregate', 'procountor_infos_aggregate', 'restructuring', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(order_by, graphql_name='address')
    bankruptcy = sgqlc.types.Field(order_by, graphql_name='bankruptcy')
    business_interruption = sgqlc.types.Field(order_by, graphql_name='business_interruption')
    eb_session_infos_aggregate = sgqlc.types.Field('eb_session_info_aggregate_order_by', graphql_name='eb_session_infos_aggregate')
    forecast_events_aggregate = sgqlc.types.Field('forecast_event_aggregate_order_by', graphql_name='forecast_events_aggregate')
    forecasts_aggregate = sgqlc.types.Field('forecast_aggregate_order_by', graphql_name='forecasts_aggregate')
    founded_date = sgqlc.types.Field(order_by, graphql_name='founded_date')
    groups_aggregate = sgqlc.types.Field('group_aggregate_order_by', graphql_name='groups_aggregate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    industry = sgqlc.types.Field(order_by, graphql_name='industry')
    invoices_by_buyer_aggregate = sgqlc.types.Field('invoice_aggregate_order_by', graphql_name='invoices_by_buyer_aggregate')
    invoices_by_seller_aggregate = sgqlc.types.Field('invoice_aggregate_order_by', graphql_name='invoices_by_seller_aggregate')
    liquidation = sgqlc.types.Field(order_by, graphql_name='liquidation')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    netvisor_infos_aggregate = sgqlc.types.Field('netvisor_info_aggregate_order_by', graphql_name='netvisor_infos_aggregate')
    procountor_infos_aggregate = sgqlc.types.Field('procountor_info_aggregate_order_by', graphql_name='procountor_infos_aggregate')
    restructuring = sgqlc.types.Field(order_by, graphql_name='restructuring')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    vat = sgqlc.types.Field(order_by, graphql_name='vat')


class company_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class company_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('address', 'bankruptcy', 'business_interruption', 'founded_date', 'id', 'industry', 'liquidation', 'name', 'restructuring', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(String, graphql_name='address')
    bankruptcy = sgqlc.types.Field(Boolean, graphql_name='bankruptcy')
    business_interruption = sgqlc.types.Field(Boolean, graphql_name='business_interruption')
    founded_date = sgqlc.types.Field(date, graphql_name='founded_date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    industry = sgqlc.types.Field(String, graphql_name='industry')
    liquidation = sgqlc.types.Field(Boolean, graphql_name='liquidation')
    name = sgqlc.types.Field(String, graphql_name='name')
    restructuring = sgqlc.types.Field(Boolean, graphql_name='restructuring')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    vat = sgqlc.types.Field(String, graphql_name='vat')


class company_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class company_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class company_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class company_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class company_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class company_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class company_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('customer_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('customer_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('customer_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('customer_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('customer_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('customer_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('customer_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('customer_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('customer_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('customer_variance_order_by', graphql_name='variance')


class customer_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('customer_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('customer_on_conflict', graphql_name='on_conflict')


class customer_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'email', 'email_subscription', 'group', 'group_id', 'id', 'password_hash', 'roles_customers', 'status', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('customer_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('customer_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('customer_bool_exp'), graphql_name='_or')
    email = sgqlc.types.Field(String_comparison_exp, graphql_name='email')
    email_subscription = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='email_subscription')
    group = sgqlc.types.Field('group_bool_exp', graphql_name='group')
    group_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='group_id')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    password_hash = sgqlc.types.Field(String_comparison_exp, graphql_name='password_hash')
    roles_customers = sgqlc.types.Field('roles_customers_bool_exp', graphql_name='roles_customers')
    status = sgqlc.types.Field(String_comparison_exp, graphql_name='status')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class customer_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Int, graphql_name='group_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class customer_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('email', 'email_subscription', 'group', 'group_id', 'id', 'password_hash', 'roles_customers', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(String, graphql_name='email')
    email_subscription = sgqlc.types.Field(Boolean, graphql_name='email_subscription')
    group = sgqlc.types.Field('group_obj_rel_insert_input', graphql_name='group')
    group_id = sgqlc.types.Field(Int, graphql_name='group_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    password_hash = sgqlc.types.Field(String, graphql_name='password_hash')
    roles_customers = sgqlc.types.Field('roles_customers_arr_rel_insert_input', graphql_name='roles_customers')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class customer_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('email', 'group_id', 'id', 'password_hash', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(order_by, graphql_name='email')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    password_hash = sgqlc.types.Field(order_by, graphql_name='password_hash')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class customer_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('email', 'group_id', 'id', 'password_hash', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(order_by, graphql_name='email')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    password_hash = sgqlc.types.Field(order_by, graphql_name='password_hash')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class customer_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(customer_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('customer_on_conflict', graphql_name='on_conflict')


class customer_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(customer_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(customer_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(customer_bool_exp, graphql_name='where')


class customer_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('email', 'email_subscription', 'group', 'group_id', 'id', 'password_hash', 'roles_customers_aggregate', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(order_by, graphql_name='email')
    email_subscription = sgqlc.types.Field(order_by, graphql_name='email_subscription')
    group = sgqlc.types.Field('group_order_by', graphql_name='group')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    password_hash = sgqlc.types.Field(order_by, graphql_name='password_hash')
    roles_customers_aggregate = sgqlc.types.Field('roles_customers_aggregate_order_by', graphql_name='roles_customers_aggregate')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class customer_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class customer_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('email', 'email_subscription', 'group_id', 'id', 'password_hash', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(String, graphql_name='email')
    email_subscription = sgqlc.types.Field(Boolean, graphql_name='email_subscription')
    group_id = sgqlc.types.Field(Int, graphql_name='group_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    password_hash = sgqlc.types.Field(String, graphql_name='password_hash')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class customer_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class customer_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(order_by, graphql_name='group_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class date_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(date, graphql_name='_eq')
    _gt = sgqlc.types.Field(date, graphql_name='_gt')
    _gte = sgqlc.types.Field(date, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(date)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(date, graphql_name='_lt')
    _lte = sgqlc.types.Field(date, graphql_name='_lte')
    _neq = sgqlc.types.Field(date, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(date)), graphql_name='_nin')


class eb_balance_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_balance_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('eb_balance_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('eb_balance_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('eb_balance_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_balance_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_balance_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_balance_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_balance_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_balance_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_balance_variance_order_by', graphql_name='variance')


class eb_balance_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_balance_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_balance_on_conflict', graphql_name='on_conflict')


class eb_balance_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_balance_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'amount', 'balance_type', 'currency', 'eb_bank_account', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('eb_balance_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('eb_balance_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('eb_balance_bool_exp'), graphql_name='_or')
    amount = sgqlc.types.Field('float8_comparison_exp', graphql_name='amount')
    balance_type = sgqlc.types.Field(String_comparison_exp, graphql_name='balance_type')
    currency = sgqlc.types.Field(String_comparison_exp, graphql_name='currency')
    eb_bank_account = sgqlc.types.Field('eb_bank_account_bool_exp', graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    last_change_date_time = sgqlc.types.Field('timestamp_comparison_exp', graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field('timestamp_comparison_exp', graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(String_comparison_exp, graphql_name='name')
    reference_date = sgqlc.types.Field(date_comparison_exp, graphql_name='reference_date')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class eb_balance_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_balance_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    balance_type = sgqlc.types.Field(String, graphql_name='balance_type')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    eb_bank_account = sgqlc.types.Field('eb_bank_account_obj_rel_insert_input', graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    last_change_date_time = sgqlc.types.Field(timestamp, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(timestamp, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(String, graphql_name='name')
    reference_date = sgqlc.types.Field(date, graphql_name='reference_date')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_balance_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    balance_type = sgqlc.types.Field(order_by, graphql_name='balance_type')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    last_change_date_time = sgqlc.types.Field(order_by, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(order_by, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    reference_date = sgqlc.types.Field(order_by, graphql_name='reference_date')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_balance_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    balance_type = sgqlc.types.Field(order_by, graphql_name='balance_type')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    last_change_date_time = sgqlc.types.Field(order_by, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(order_by, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    reference_date = sgqlc.types.Field(order_by, graphql_name='reference_date')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_balance_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(eb_balance_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_balance_on_conflict', graphql_name='on_conflict')


class eb_balance_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(eb_balance_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(eb_balance_bool_exp, graphql_name='where')


class eb_balance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    balance_type = sgqlc.types.Field(order_by, graphql_name='balance_type')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    eb_bank_account = sgqlc.types.Field('eb_bank_account_order_by', graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    last_change_date_time = sgqlc.types.Field(order_by, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(order_by, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    reference_date = sgqlc.types.Field(order_by, graphql_name='reference_date')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_balance_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class eb_balance_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    balance_type = sgqlc.types.Field(String, graphql_name='balance_type')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    last_change_date_time = sgqlc.types.Field(timestamp, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(timestamp, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(String, graphql_name='name')
    reference_date = sgqlc.types.Field(date, graphql_name='reference_date')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_balance_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_balance_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_balance_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_balance_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_balance_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_balance_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_balance_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_bank_account_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('eb_bank_account_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('eb_bank_account_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('eb_bank_account_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_bank_account_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_bank_account_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_bank_account_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_bank_account_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_bank_account_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_bank_account_variance_order_by', graphql_name='variance')


class eb_bank_account_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_bank_account_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_bank_account_on_conflict', graphql_name='on_conflict')


class eb_bank_account_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'account_uid', 'eb_balances', 'eb_session_info', 'eb_session_info_id', 'eb_transactions', 'id', 'identification_hash', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('eb_bank_account_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('eb_bank_account_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('eb_bank_account_bool_exp'), graphql_name='_or')
    account_uid = sgqlc.types.Field(String_comparison_exp, graphql_name='account_uid')
    eb_balances = sgqlc.types.Field(eb_balance_bool_exp, graphql_name='eb_balances')
    eb_session_info = sgqlc.types.Field('eb_session_info_bool_exp', graphql_name='eb_session_info')
    eb_session_info_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='eb_session_info_id')
    eb_transactions = sgqlc.types.Field('eb_transaction_bool_exp', graphql_name='eb_transactions')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    identification_hash = sgqlc.types.Field(String_comparison_exp, graphql_name='identification_hash')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class eb_bank_account_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Int, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_bank_account_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_balances', 'eb_session_info', 'eb_session_info_id', 'eb_transactions', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(String, graphql_name='account_uid')
    eb_balances = sgqlc.types.Field(eb_balance_arr_rel_insert_input, graphql_name='eb_balances')
    eb_session_info = sgqlc.types.Field('eb_session_info_obj_rel_insert_input', graphql_name='eb_session_info')
    eb_session_info_id = sgqlc.types.Field(Int, graphql_name='eb_session_info_id')
    eb_transactions = sgqlc.types.Field('eb_transaction_arr_rel_insert_input', graphql_name='eb_transactions')
    id = sgqlc.types.Field(Int, graphql_name='id')
    identification_hash = sgqlc.types.Field(String, graphql_name='identification_hash')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_bank_account_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_session_info_id', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(order_by, graphql_name='account_uid')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    identification_hash = sgqlc.types.Field(order_by, graphql_name='identification_hash')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_bank_account_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_session_info_id', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(order_by, graphql_name='account_uid')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    identification_hash = sgqlc.types.Field(order_by, graphql_name='identification_hash')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_bank_account_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(eb_bank_account_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_bank_account_on_conflict', graphql_name='on_conflict')


class eb_bank_account_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(eb_bank_account_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(eb_bank_account_bool_exp, graphql_name='where')


class eb_bank_account_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_balances_aggregate', 'eb_session_info', 'eb_session_info_id', 'eb_transactions_aggregate', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(order_by, graphql_name='account_uid')
    eb_balances_aggregate = sgqlc.types.Field(eb_balance_aggregate_order_by, graphql_name='eb_balances_aggregate')
    eb_session_info = sgqlc.types.Field('eb_session_info_order_by', graphql_name='eb_session_info')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    eb_transactions_aggregate = sgqlc.types.Field('eb_transaction_aggregate_order_by', graphql_name='eb_transactions_aggregate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    identification_hash = sgqlc.types.Field(order_by, graphql_name='identification_hash')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_bank_account_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class eb_bank_account_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_session_info_id', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(String, graphql_name='account_uid')
    eb_session_info_id = sgqlc.types.Field(Int, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    identification_hash = sgqlc.types.Field(String, graphql_name='identification_hash')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_bank_account_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_bank_account_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(order_by, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_keys_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('eb_keys_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('eb_keys_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('eb_keys_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_keys_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_keys_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_keys_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_keys_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_keys_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_keys_variance_order_by', graphql_name='variance')


class eb_keys_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_keys_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_keys_on_conflict', graphql_name='on_conflict')


class eb_keys_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('eb_keys_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('eb_keys_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('eb_keys_bool_exp'), graphql_name='_or')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    private_key = sgqlc.types.Field(String_comparison_exp, graphql_name='private_key')
    public_cert = sgqlc.types.Field(String_comparison_exp, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(String_comparison_exp, graphql_name='public_pem')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class eb_keys_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_keys_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(Int, graphql_name='id')
    private_key = sgqlc.types.Field(String, graphql_name='private_key')
    public_cert = sgqlc.types.Field(String, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(String, graphql_name='public_pem')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_keys_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    private_key = sgqlc.types.Field(order_by, graphql_name='private_key')
    public_cert = sgqlc.types.Field(order_by, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(order_by, graphql_name='public_pem')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_keys_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    private_key = sgqlc.types.Field(order_by, graphql_name='private_key')
    public_cert = sgqlc.types.Field(order_by, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(order_by, graphql_name='public_pem')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_keys_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(eb_keys_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_keys_on_conflict', graphql_name='on_conflict')


class eb_keys_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(eb_keys_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(eb_keys_bool_exp, graphql_name='where')


class eb_keys_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    private_key = sgqlc.types.Field(order_by, graphql_name='private_key')
    public_cert = sgqlc.types.Field(order_by, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(order_by, graphql_name='public_pem')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class eb_keys_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class eb_keys_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(Int, graphql_name='id')
    private_key = sgqlc.types.Field(String, graphql_name='private_key')
    public_cert = sgqlc.types.Field(String, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(String, graphql_name='public_pem')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_keys_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_keys_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_session_info_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('eb_session_info_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('eb_session_info_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('eb_session_info_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_session_info_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_session_info_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_session_info_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_session_info_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_session_info_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_session_info_variance_order_by', graphql_name='variance')


class eb_session_info_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_session_info_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_session_info_on_conflict', graphql_name='on_conflict')


class eb_session_info_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'company', 'company_id', 'eb_bank_accounts', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    _and = sgqlc.types.Field(sgqlc.types.list_of('eb_session_info_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('eb_session_info_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('eb_session_info_bool_exp'), graphql_name='_or')
    company = sgqlc.types.Field(company_bool_exp, graphql_name='company')
    company_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='company_id')
    eb_bank_accounts = sgqlc.types.Field(eb_bank_account_bool_exp, graphql_name='eb_bank_accounts')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    session_id = sgqlc.types.Field(String_comparison_exp, graphql_name='session_id')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')
    valid_until = sgqlc.types.Field(date_comparison_exp, graphql_name='valid_until')


class eb_session_info_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_session_info_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'eb_bank_accounts', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    eb_bank_accounts = sgqlc.types.Field(eb_bank_account_arr_rel_insert_input, graphql_name='eb_bank_accounts')
    id = sgqlc.types.Field(Int, graphql_name='id')
    session_id = sgqlc.types.Field(String, graphql_name='session_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(date, graphql_name='valid_until')


class eb_session_info_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    session_id = sgqlc.types.Field(order_by, graphql_name='session_id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(order_by, graphql_name='valid_until')


class eb_session_info_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    session_id = sgqlc.types.Field(order_by, graphql_name='session_id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(order_by, graphql_name='valid_until')


class eb_session_info_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(eb_session_info_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_session_info_on_conflict', graphql_name='on_conflict')


class eb_session_info_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(eb_session_info_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(eb_session_info_bool_exp, graphql_name='where')


class eb_session_info_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'eb_bank_accounts_aggregate', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company = sgqlc.types.Field(company_order_by, graphql_name='company')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    eb_bank_accounts_aggregate = sgqlc.types.Field(eb_bank_account_aggregate_order_by, graphql_name='eb_bank_accounts_aggregate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    session_id = sgqlc.types.Field(order_by, graphql_name='session_id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(order_by, graphql_name='valid_until')


class eb_session_info_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class eb_session_info_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    session_id = sgqlc.types.Field(String, graphql_name='session_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(date, graphql_name='valid_until')


class eb_session_info_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_session_info_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_transaction_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('eb_transaction_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('eb_transaction_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('eb_transaction_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_transaction_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_transaction_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_transaction_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_transaction_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_transaction_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_transaction_variance_order_by', graphql_name='variance')


class eb_transaction_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_transaction_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_transaction_on_conflict', graphql_name='on_conflict')


class eb_transaction_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    _and = sgqlc.types.Field(sgqlc.types.list_of('eb_transaction_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('eb_transaction_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('eb_transaction_bool_exp'), graphql_name='_or')
    amount = sgqlc.types.Field('float8_comparison_exp', graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(String_comparison_exp, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(String_comparison_exp, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(String_comparison_exp, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(date_comparison_exp, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(String_comparison_exp, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(String_comparison_exp, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(String_comparison_exp, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(String_comparison_exp, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account = sgqlc.types.Field(eb_bank_account_bool_exp, graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(String_comparison_exp, graphql_name='entry_reference')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(String_comparison_exp, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(String_comparison_exp, graphql_name='remittance_information')
    status = sgqlc.types.Field(String_comparison_exp, graphql_name='status')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(date_comparison_exp, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(date_comparison_exp, graphql_name='value_date')


class eb_transaction_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_transaction_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(String, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(date, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(String, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(String, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(String, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(String, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(String, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(String, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(String, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(String, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(String, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(String, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(String, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account = sgqlc.types.Field(eb_bank_account_obj_rel_insert_input, graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(String, graphql_name='entry_reference')
    id = sgqlc.types.Field(Int, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(String, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(String, graphql_name='remittance_information')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(date, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(date, graphql_name='value_date')


class eb_transaction_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(order_by, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(order_by, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(order_by, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(order_by, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(order_by, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(order_by, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(order_by, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(order_by, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(order_by, graphql_name='entry_reference')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(order_by, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(order_by, graphql_name='remittance_information')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(order_by, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(order_by, graphql_name='value_date')


class eb_transaction_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(order_by, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(order_by, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(order_by, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(order_by, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(order_by, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(order_by, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(order_by, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(order_by, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(order_by, graphql_name='entry_reference')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(order_by, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(order_by, graphql_name='remittance_information')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(order_by, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(order_by, graphql_name='value_date')


class eb_transaction_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(eb_transaction_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('eb_transaction_on_conflict', graphql_name='on_conflict')


class eb_transaction_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(eb_transaction_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(eb_transaction_bool_exp, graphql_name='where')


class eb_transaction_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(order_by, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(order_by, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(order_by, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(order_by, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(order_by, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(order_by, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(order_by, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(order_by, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(order_by, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(order_by, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account = sgqlc.types.Field(eb_bank_account_order_by, graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(order_by, graphql_name='entry_reference')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(order_by, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(order_by, graphql_name='remittance_information')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(order_by, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(order_by, graphql_name='value_date')


class eb_transaction_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class eb_transaction_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(String, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(date, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(String, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(String, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(String, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(String, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(String, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(String, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(String, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(String, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(String, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(String, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(String, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(String, graphql_name='entry_reference')
    id = sgqlc.types.Field(Int, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(String, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(String, graphql_name='remittance_information')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(date, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(date, graphql_name='value_date')


class eb_transaction_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class eb_transaction_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(order_by, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class float8_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(float8, graphql_name='_eq')
    _gt = sgqlc.types.Field(float8, graphql_name='_gt')
    _gte = sgqlc.types.Field(float8, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(float8)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(float8, graphql_name='_lt')
    _lte = sgqlc.types.Field(float8, graphql_name='_lte')
    _neq = sgqlc.types.Field(float8, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(float8)), graphql_name='_nin')


class forecast_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('forecast_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('forecast_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('forecast_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('forecast_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('forecast_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('forecast_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('forecast_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('forecast_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('forecast_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('forecast_variance_order_by', graphql_name='variance')


class forecast_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('forecast_on_conflict', graphql_name='on_conflict')


class forecast_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'company', 'company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    _and = sgqlc.types.Field(sgqlc.types.list_of('forecast_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('forecast_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('forecast_bool_exp'), graphql_name='_or')
    company = sgqlc.types.Field(company_bool_exp, graphql_name='company')
    company_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='company_id')
    date = sgqlc.types.Field(date_comparison_exp, graphql_name='date')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    lower_bound = sgqlc.types.Field(float8_comparison_exp, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8_comparison_exp, graphql_name='median')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(float8_comparison_exp, graphql_name='upper_bound')


class forecast_event_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('forecast_event_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('forecast_event_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('forecast_event_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('forecast_event_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('forecast_event_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('forecast_event_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('forecast_event_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('forecast_event_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('forecast_event_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('forecast_event_variance_order_by', graphql_name='variance')


class forecast_event_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast_event_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('forecast_event_on_conflict', graphql_name='on_conflict')


class forecast_event_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_event_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'company', 'company_id', 'data', 'event_class', 'id', 'invoice_type_enum', 'time_created', 'time_updated', 'type')
    _and = sgqlc.types.Field(sgqlc.types.list_of('forecast_event_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('forecast_event_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('forecast_event_bool_exp'), graphql_name='_or')
    company = sgqlc.types.Field(company_bool_exp, graphql_name='company')
    company_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='company_id')
    data = sgqlc.types.Field(String_comparison_exp, graphql_name='data')
    event_class = sgqlc.types.Field(String_comparison_exp, graphql_name='event_class')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    invoice_type_enum = sgqlc.types.Field('invoice_type_enum_bool_exp', graphql_name='invoice_type_enum')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')
    type = sgqlc.types.Field('invoice_type_enum_enum_comparison_exp', graphql_name='type')


class forecast_event_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class forecast_event_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'data', 'event_class', 'id', 'invoice_type_enum', 'time_created', 'time_updated', 'type')
    company = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    data = sgqlc.types.Field(String, graphql_name='data')
    event_class = sgqlc.types.Field(String, graphql_name='event_class')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice_type_enum = sgqlc.types.Field('invoice_type_enum_obj_rel_insert_input', graphql_name='invoice_type_enum')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    type = sgqlc.types.Field(invoice_type_enum_enum, graphql_name='type')


class forecast_event_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'data', 'event_class', 'id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    data = sgqlc.types.Field(order_by, graphql_name='data')
    event_class = sgqlc.types.Field(order_by, graphql_name='event_class')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class forecast_event_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'data', 'event_class', 'id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    data = sgqlc.types.Field(order_by, graphql_name='data')
    event_class = sgqlc.types.Field(order_by, graphql_name='event_class')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class forecast_event_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(forecast_event_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('forecast_event_on_conflict', graphql_name='on_conflict')


class forecast_event_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(forecast_event_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(forecast_event_bool_exp, graphql_name='where')


class forecast_event_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'data', 'event_class', 'id', 'invoice_type_enum', 'time_created', 'time_updated', 'type')
    company = sgqlc.types.Field(company_order_by, graphql_name='company')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    data = sgqlc.types.Field(order_by, graphql_name='data')
    event_class = sgqlc.types.Field(order_by, graphql_name='event_class')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_type_enum = sgqlc.types.Field('invoice_type_enum_order_by', graphql_name='invoice_type_enum')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    type = sgqlc.types.Field(order_by, graphql_name='type')


class forecast_event_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class forecast_event_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'data', 'event_class', 'id', 'time_created', 'time_updated', 'type')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    data = sgqlc.types.Field(String, graphql_name='data')
    event_class = sgqlc.types.Field(String, graphql_name='event_class')
    id = sgqlc.types.Field(Int, graphql_name='id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    type = sgqlc.types.Field(invoice_type_enum_enum, graphql_name='type')


class forecast_event_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_event_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_event_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_event_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_event_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_event_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_event_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class forecast_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    lower_bound = sgqlc.types.Field(float8, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8, graphql_name='median')
    upper_bound = sgqlc.types.Field(float8, graphql_name='upper_bound')


class forecast_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    date = sgqlc.types.Field('date', graphql_name='date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    lower_bound = sgqlc.types.Field(float8, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8, graphql_name='median')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(float8, graphql_name='upper_bound')


class forecast_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    date = sgqlc.types.Field(order_by, graphql_name='date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    date = sgqlc.types.Field(order_by, graphql_name='date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(forecast_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('forecast_on_conflict', graphql_name='on_conflict')


class forecast_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(forecast_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(forecast_bool_exp, graphql_name='where')


class forecast_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company = sgqlc.types.Field(company_order_by, graphql_name='company')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    date = sgqlc.types.Field(order_by, graphql_name='date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class forecast_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    date = sgqlc.types.Field('date', graphql_name='date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    lower_bound = sgqlc.types.Field(float8, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8, graphql_name='median')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(float8, graphql_name='upper_bound')


class forecast_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class forecast_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    lower_bound = sgqlc.types.Field(order_by, graphql_name='lower_bound')
    median = sgqlc.types.Field(order_by, graphql_name='median')
    upper_bound = sgqlc.types.Field(order_by, graphql_name='upper_bound')


class group_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('group_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('group_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('group_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('group_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('group_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('group_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('group_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('group_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('group_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('group_variance_order_by', graphql_name='variance')


class group_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('group_on_conflict', graphql_name='on_conflict')


class group_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class group_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'company', 'company_id', 'customers', 'group_relations_by_primary', 'group_relations_by_secondary', 'id', 'name', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('group_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('group_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('group_bool_exp'), graphql_name='_or')
    company = sgqlc.types.Field(company_bool_exp, graphql_name='company')
    company_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='company_id')
    customers = sgqlc.types.Field(customer_bool_exp, graphql_name='customers')
    group_relations_by_primary = sgqlc.types.Field('group_relation_bool_exp', graphql_name='group_relations_by_primary')
    group_relations_by_secondary = sgqlc.types.Field('group_relation_bool_exp', graphql_name='group_relations_by_secondary')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    name = sgqlc.types.Field(String_comparison_exp, graphql_name='name')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class group_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class group_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'customers', 'group_relations_by_primary', 'group_relations_by_secondary', 'id', 'name', 'time_created', 'time_updated')
    company = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    customers = sgqlc.types.Field(customer_arr_rel_insert_input, graphql_name='customers')
    group_relations_by_primary = sgqlc.types.Field('group_relation_arr_rel_insert_input', graphql_name='group_relations_by_primary')
    group_relations_by_secondary = sgqlc.types.Field('group_relation_arr_rel_insert_input', graphql_name='group_relations_by_secondary')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class group_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'name', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class group_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'name', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class group_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(group_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('group_on_conflict', graphql_name='on_conflict')


class group_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(group_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(group_bool_exp, graphql_name='where')


class group_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'customers_aggregate', 'group_relations_by_primary_aggregate', 'group_relations_by_secondary_aggregate', 'id', 'name', 'time_created', 'time_updated')
    company = sgqlc.types.Field(company_order_by, graphql_name='company')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    customers_aggregate = sgqlc.types.Field(customer_aggregate_order_by, graphql_name='customers_aggregate')
    group_relations_by_primary_aggregate = sgqlc.types.Field('group_relation_aggregate_order_by', graphql_name='group_relations_by_primary_aggregate')
    group_relations_by_secondary_aggregate = sgqlc.types.Field('group_relation_aggregate_order_by', graphql_name='group_relations_by_secondary_aggregate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class group_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class group_relation_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('group_relation_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('group_relation_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('group_relation_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('group_relation_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('group_relation_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('group_relation_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('group_relation_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('group_relation_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('group_relation_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('group_relation_variance_order_by', graphql_name='variance')


class group_relation_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group_relation_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('group_relation_on_conflict', graphql_name='on_conflict')


class group_relation_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'group_by_primary', 'group_by_secondary', 'primary_id', 'secondary_id')
    _and = sgqlc.types.Field(sgqlc.types.list_of('group_relation_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('group_relation_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('group_relation_bool_exp'), graphql_name='_or')
    group_by_primary = sgqlc.types.Field(group_bool_exp, graphql_name='group_by_primary')
    group_by_secondary = sgqlc.types.Field(group_bool_exp, graphql_name='group_by_secondary')
    primary_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='secondary_id')


class group_relation_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Int, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Int, graphql_name='secondary_id')


class group_relation_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_by_primary', 'group_by_secondary', 'primary_id', 'secondary_id')
    group_by_primary = sgqlc.types.Field(group_obj_rel_insert_input, graphql_name='group_by_primary')
    group_by_secondary = sgqlc.types.Field(group_obj_rel_insert_input, graphql_name='group_by_secondary')
    primary_id = sgqlc.types.Field(Int, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Int, graphql_name='secondary_id')


class group_relation_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(group_relation_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('group_relation_on_conflict', graphql_name='on_conflict')


class group_relation_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(group_relation_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(group_relation_bool_exp, graphql_name='where')


class group_relation_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('group_by_primary', 'group_by_secondary', 'primary_id', 'secondary_id')
    group_by_primary = sgqlc.types.Field(group_order_by, graphql_name='group_by_primary')
    group_by_secondary = sgqlc.types.Field(group_order_by, graphql_name='group_by_secondary')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='secondary_id')


class group_relation_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Int, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Int, graphql_name='secondary_id')


class group_relation_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_relation_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(order_by, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(order_by, graphql_name='secondary_id')


class group_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'name', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class group_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class group_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class group_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class group_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class group_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class group_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class group_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class invoice_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('invoice_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('invoice_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('invoice_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('invoice_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('invoice_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('invoice_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('invoice_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('invoice_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('invoice_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('invoice_variance_order_by', graphql_name='variance')


class invoice_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('invoice_on_conflict', graphql_name='on_conflict')


class invoice_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class invoice_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'amount', 'buyer', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'invoice_type_enum', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'payments', 'provider_status', 'reference_number', 'seller', 'seller_id', 'source', 'source_enum', 'status', 'time_created', 'time_updated', 'type')
    _and = sgqlc.types.Field(sgqlc.types.list_of('invoice_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('invoice_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('invoice_bool_exp'), graphql_name='_or')
    amount = sgqlc.types.Field(float8_comparison_exp, graphql_name='amount')
    buyer = sgqlc.types.Field(company_bool_exp, graphql_name='buyer')
    buyer_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(String_comparison_exp, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(String_comparison_exp, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(float8_comparison_exp, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8_comparison_exp, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(date_comparison_exp, graphql_name='create_date')
    currency = sgqlc.types.Field(String_comparison_exp, graphql_name='currency')
    currency_rate = sgqlc.types.Field(float8_comparison_exp, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(date_comparison_exp, graphql_name='due_date')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    invoice_type_enum = sgqlc.types.Field('invoice_type_enum_bool_exp', graphql_name='invoice_type_enum')
    original_amount = sgqlc.types.Field(float8_comparison_exp, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8_comparison_exp, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(date_comparison_exp, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(float8_comparison_exp, graphql_name='payment_term_percentage')
    payments = sgqlc.types.Field('payment_bool_exp', graphql_name='payments')
    provider_status = sgqlc.types.Field(String_comparison_exp, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(String_comparison_exp, graphql_name='reference_number')
    seller = sgqlc.types.Field(company_bool_exp, graphql_name='seller')
    seller_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='seller_id')
    source = sgqlc.types.Field('source_enum_enum_comparison_exp', graphql_name='source')
    source_enum = sgqlc.types.Field('source_enum_bool_exp', graphql_name='source_enum')
    status = sgqlc.types.Field(String_comparison_exp, graphql_name='status')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')
    type = sgqlc.types.Field('invoice_type_enum_enum_comparison_exp', graphql_name='type')


class invoice_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Int, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(float8, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(float8, graphql_name='currency_rate')
    id = sgqlc.types.Field(Int, graphql_name='id')
    original_amount = sgqlc.types.Field(float8, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(float8, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Int, graphql_name='seller_id')


class invoice_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'invoice_type_enum', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'payments', 'provider_status', 'reference_number', 'seller', 'seller_id', 'source', 'source_enum', 'status', 'time_created', 'time_updated', 'type')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    buyer = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='buyer')
    buyer_id = sgqlc.types.Field(Int, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(String, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(String, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(float8, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(date, graphql_name='create_date')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    currency_rate = sgqlc.types.Field(float8, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(date, graphql_name='due_date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice_type_enum = sgqlc.types.Field('invoice_type_enum_obj_rel_insert_input', graphql_name='invoice_type_enum')
    original_amount = sgqlc.types.Field(float8, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(float8, graphql_name='payment_term_percentage')
    payments = sgqlc.types.Field('payment_arr_rel_insert_input', graphql_name='payments')
    provider_status = sgqlc.types.Field(String, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    seller = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='seller')
    seller_id = sgqlc.types.Field(Int, graphql_name='seller_id')
    source = sgqlc.types.Field(source_enum_enum, graphql_name='source')
    source_enum = sgqlc.types.Field('source_enum_obj_rel_insert_input', graphql_name='source_enum')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    type = sgqlc.types.Field(invoice_type_enum_enum, graphql_name='type')


class invoice_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'provider_status', 'reference_number', 'seller_id', 'status', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(order_by, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(order_by, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(order_by, graphql_name='create_date')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(order_by, graphql_name='due_date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(order_by, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    provider_status = sgqlc.types.Field(order_by, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(order_by, graphql_name='reference_number')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class invoice_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'provider_status', 'reference_number', 'seller_id', 'status', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(order_by, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(order_by, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(order_by, graphql_name='create_date')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(order_by, graphql_name='due_date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(order_by, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    provider_status = sgqlc.types.Field(order_by, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(order_by, graphql_name='reference_number')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class invoice_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(invoice_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('invoice_on_conflict', graphql_name='on_conflict')


class invoice_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(invoice_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(invoice_bool_exp, graphql_name='where')


class invoice_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'invoice_type_enum', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'payments_aggregate', 'provider_status', 'reference_number', 'seller', 'seller_id', 'source', 'source_enum', 'status', 'time_created', 'time_updated', 'type')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer = sgqlc.types.Field(company_order_by, graphql_name='buyer')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(order_by, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(order_by, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(order_by, graphql_name='create_date')
    currency = sgqlc.types.Field(order_by, graphql_name='currency')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(order_by, graphql_name='due_date')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_type_enum = sgqlc.types.Field('invoice_type_enum_order_by', graphql_name='invoice_type_enum')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(order_by, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    payments_aggregate = sgqlc.types.Field('payment_aggregate_order_by', graphql_name='payments_aggregate')
    provider_status = sgqlc.types.Field(order_by, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(order_by, graphql_name='reference_number')
    seller = sgqlc.types.Field(company_order_by, graphql_name='seller')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')
    source = sgqlc.types.Field(order_by, graphql_name='source')
    source_enum = sgqlc.types.Field('source_enum_order_by', graphql_name='source_enum')
    status = sgqlc.types.Field(order_by, graphql_name='status')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')
    type = sgqlc.types.Field(order_by, graphql_name='type')


class invoice_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class invoice_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'provider_status', 'reference_number', 'seller_id', 'source', 'status', 'time_created', 'time_updated', 'type')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Int, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(String, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(String, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(float8, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(date, graphql_name='create_date')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    currency_rate = sgqlc.types.Field(float8, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(date, graphql_name='due_date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    original_amount = sgqlc.types.Field(float8, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(float8, graphql_name='payment_term_percentage')
    provider_status = sgqlc.types.Field(String, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    seller_id = sgqlc.types.Field(Int, graphql_name='seller_id')
    source = sgqlc.types.Field(source_enum_enum, graphql_name='source')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    type = sgqlc.types.Field(invoice_type_enum_enum, graphql_name='type')


class invoice_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class invoice_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class invoice_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class invoice_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class invoice_type_enum_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('count', 'max', 'min')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('invoice_type_enum_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('invoice_type_enum_min_order_by', graphql_name='min')


class invoice_type_enum_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice_type_enum_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('invoice_type_enum_on_conflict', graphql_name='on_conflict')


class invoice_type_enum_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'forecast_events', 'id', 'invoices')
    _and = sgqlc.types.Field(sgqlc.types.list_of('invoice_type_enum_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('invoice_type_enum_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('invoice_type_enum_bool_exp'), graphql_name='_or')
    forecast_events = sgqlc.types.Field(forecast_event_bool_exp, graphql_name='forecast_events')
    id = sgqlc.types.Field(String_comparison_exp, graphql_name='id')
    invoices = sgqlc.types.Field(invoice_bool_exp, graphql_name='invoices')


class invoice_type_enum_enum_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_in', '_is_null', '_neq', '_nin')
    _eq = sgqlc.types.Field(invoice_type_enum_enum, graphql_name='_eq')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_enum)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _neq = sgqlc.types.Field(invoice_type_enum_enum, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_enum)), graphql_name='_nin')


class invoice_type_enum_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('forecast_events', 'id', 'invoices')
    forecast_events = sgqlc.types.Field(forecast_event_arr_rel_insert_input, graphql_name='forecast_events')
    id = sgqlc.types.Field(String, graphql_name='id')
    invoices = sgqlc.types.Field(invoice_arr_rel_insert_input, graphql_name='invoices')


class invoice_type_enum_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class invoice_type_enum_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class invoice_type_enum_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(invoice_type_enum_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('invoice_type_enum_on_conflict', graphql_name='on_conflict')


class invoice_type_enum_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(invoice_type_enum_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(invoice_type_enum_bool_exp, graphql_name='where')


class invoice_type_enum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('forecast_events_aggregate', 'id', 'invoices_aggregate')
    forecast_events_aggregate = sgqlc.types.Field(forecast_event_aggregate_order_by, graphql_name='forecast_events_aggregate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoices_aggregate = sgqlc.types.Field(invoice_aggregate_order_by, graphql_name='invoices_aggregate')


class invoice_type_enum_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class invoice_type_enum_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(String, graphql_name='id')


class invoice_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class invoice_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class invoice_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    buyer_id = sgqlc.types.Field(order_by, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(order_by, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(order_by, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(order_by, graphql_name='currency_rate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    original_amount = sgqlc.types.Field(order_by, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(order_by, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(order_by, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(order_by, graphql_name='seller_id')


class netvisor_info_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('netvisor_info_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('netvisor_info_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('netvisor_info_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('netvisor_info_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('netvisor_info_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('netvisor_info_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('netvisor_info_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('netvisor_info_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('netvisor_info_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('netvisor_info_variance_order_by', graphql_name='variance')


class netvisor_info_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('netvisor_info_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('netvisor_info_on_conflict', graphql_name='on_conflict')


class netvisor_info_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class netvisor_info_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'company', 'company_id', 'id', 'is_active', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('netvisor_info_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('netvisor_info_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('netvisor_info_bool_exp'), graphql_name='_or')
    company = sgqlc.types.Field(company_bool_exp, graphql_name='company')
    company_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='company_id')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    is_active = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='is_active')
    netvisor_customer_id = sgqlc.types.Field(String_comparison_exp, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(String_comparison_exp, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(String_comparison_exp, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class netvisor_info_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class netvisor_info_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'id', 'is_active', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')
    netvisor_customer_id = sgqlc.types.Field(String, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(String, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(String, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class netvisor_info_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    netvisor_customer_id = sgqlc.types.Field(order_by, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(order_by, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(order_by, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class netvisor_info_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    netvisor_customer_id = sgqlc.types.Field(order_by, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(order_by, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(order_by, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class netvisor_info_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(netvisor_info_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('netvisor_info_on_conflict', graphql_name='on_conflict')


class netvisor_info_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(netvisor_info_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(netvisor_info_bool_exp, graphql_name='where')


class netvisor_info_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'id', 'is_active', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company = sgqlc.types.Field(company_order_by, graphql_name='company')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    is_active = sgqlc.types.Field(order_by, graphql_name='is_active')
    netvisor_customer_id = sgqlc.types.Field(order_by, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(order_by, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(order_by, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class netvisor_info_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class netvisor_info_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'is_active', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')
    netvisor_customer_id = sgqlc.types.Field(String, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(String, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(String, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class netvisor_info_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class netvisor_info_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class netvisor_info_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class netvisor_info_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class netvisor_info_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class netvisor_info_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class netvisor_info_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class payment_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('payment_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('payment_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('payment_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('payment_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('payment_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('payment_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('payment_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('payment_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('payment_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('payment_variance_order_by', graphql_name='variance')


class payment_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('payment_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('payment_on_conflict', graphql_name='on_conflict')


class payment_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class payment_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'amount', 'id', 'invoice', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('payment_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('payment_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('payment_bool_exp'), graphql_name='_or')
    amount = sgqlc.types.Field(float8_comparison_exp, graphql_name='amount')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    invoice = sgqlc.types.Field(invoice_bool_exp, graphql_name='invoice')
    invoice_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(date_comparison_exp, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(String_comparison_exp, graphql_name='reference_number')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class payment_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice_id = sgqlc.types.Field(Int, graphql_name='invoice_id')


class payment_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice = sgqlc.types.Field(invoice_obj_rel_insert_input, graphql_name='invoice')
    invoice_id = sgqlc.types.Field(Int, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class payment_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(order_by, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(order_by, graphql_name='reference_number')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class payment_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(order_by, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(order_by, graphql_name='reference_number')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class payment_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(payment_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('payment_on_conflict', graphql_name='on_conflict')


class payment_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(payment_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(payment_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(payment_bool_exp, graphql_name='where')


class payment_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice = sgqlc.types.Field(invoice_order_by, graphql_name='invoice')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(order_by, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(order_by, graphql_name='reference_number')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class payment_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class payment_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice_id = sgqlc.types.Field(Int, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class payment_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class payment_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class payment_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class payment_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class payment_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class payment_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class payment_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(order_by, graphql_name='amount')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoice_id = sgqlc.types.Field(order_by, graphql_name='invoice_id')


class procountor_info_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('procountor_info_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('procountor_info_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('procountor_info_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('procountor_info_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('procountor_info_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('procountor_info_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('procountor_info_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('procountor_info_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('procountor_info_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('procountor_info_variance_order_by', graphql_name='variance')


class procountor_info_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('procountor_info_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('procountor_info_on_conflict', graphql_name='on_conflict')


class procountor_info_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class procountor_info_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'company', 'company_id', 'id', 'is_active', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('procountor_info_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('procountor_info_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('procountor_info_bool_exp'), graphql_name='_or')
    company = sgqlc.types.Field(company_bool_exp, graphql_name='company')
    company_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='company_id')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    is_active = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='is_active')
    procountor_refresh_token = sgqlc.types.Field(String_comparison_exp, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(String_comparison_exp, graphql_name='procountor_token')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class procountor_info_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class procountor_info_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'id', 'is_active', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company = sgqlc.types.Field(company_obj_rel_insert_input, graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')
    procountor_refresh_token = sgqlc.types.Field(String, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(String, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class procountor_info_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    procountor_refresh_token = sgqlc.types.Field(order_by, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(order_by, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class procountor_info_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    procountor_refresh_token = sgqlc.types.Field(order_by, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(order_by, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class procountor_info_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(procountor_info_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('procountor_info_on_conflict', graphql_name='on_conflict')


class procountor_info_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(procountor_info_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(procountor_info_bool_exp, graphql_name='where')


class procountor_info_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'id', 'is_active', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company = sgqlc.types.Field(company_order_by, graphql_name='company')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    is_active = sgqlc.types.Field(order_by, graphql_name='is_active')
    procountor_refresh_token = sgqlc.types.Field(order_by, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(order_by, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class procountor_info_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class procountor_info_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'is_active', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')
    procountor_refresh_token = sgqlc.types.Field(String, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(String, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class procountor_info_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class procountor_info_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class procountor_info_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class procountor_info_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class procountor_info_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class procountor_info_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class procountor_info_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(order_by, graphql_name='company_id')
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('role_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('role_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('role_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('role_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('role_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('role_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('role_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('role_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('role_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('role_variance_order_by', graphql_name='variance')


class role_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('role_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('role_on_conflict', graphql_name='on_conflict')


class role_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'description', 'id', 'name', 'roles_customers', 'time_created', 'time_updated')
    _and = sgqlc.types.Field(sgqlc.types.list_of('role_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('role_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('role_bool_exp'), graphql_name='_or')
    description = sgqlc.types.Field(String_comparison_exp, graphql_name='description')
    id = sgqlc.types.Field(Int_comparison_exp, graphql_name='id')
    name = sgqlc.types.Field(String_comparison_exp, graphql_name='name')
    roles_customers = sgqlc.types.Field('roles_customers_bool_exp', graphql_name='roles_customers')
    time_created = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_created')
    time_updated = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='time_updated')


class role_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Int, graphql_name='id')


class role_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'roles_customers', 'time_created', 'time_updated')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    roles_customers = sgqlc.types.Field('roles_customers_arr_rel_insert_input', graphql_name='roles_customers')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class role_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'time_created', 'time_updated')
    description = sgqlc.types.Field(order_by, graphql_name='description')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class role_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'time_created', 'time_updated')
    description = sgqlc.types.Field(order_by, graphql_name='description')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class role_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(role_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('role_on_conflict', graphql_name='on_conflict')


class role_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(role_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(role_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(role_bool_exp, graphql_name='where')


class role_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'roles_customers_aggregate', 'time_created', 'time_updated')
    description = sgqlc.types.Field(order_by, graphql_name='description')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    roles_customers_aggregate = sgqlc.types.Field('roles_customers_aggregate_order_by', graphql_name='roles_customers_aggregate')
    time_created = sgqlc.types.Field(order_by, graphql_name='time_created')
    time_updated = sgqlc.types.Field(order_by, graphql_name='time_updated')


class role_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class role_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'time_created', 'time_updated')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class role_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class role_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class roles_customers_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('roles_customers_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('roles_customers_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('roles_customers_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('roles_customers_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('roles_customers_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('roles_customers_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('roles_customers_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('roles_customers_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('roles_customers_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('roles_customers_variance_order_by', graphql_name='variance')


class roles_customers_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('roles_customers_insert_input'))), graphql_name='data')


class roles_customers_avg_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'customer', 'role', 'role_id', 'user_id')
    _and = sgqlc.types.Field(sgqlc.types.list_of('roles_customers_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('roles_customers_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('roles_customers_bool_exp'), graphql_name='_or')
    customer = sgqlc.types.Field(customer_bool_exp, graphql_name='customer')
    role = sgqlc.types.Field(role_bool_exp, graphql_name='role')
    role_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int_comparison_exp, graphql_name='user_id')


class roles_customers_inc_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')


class roles_customers_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('customer', 'role', 'role_id', 'user_id')
    customer = sgqlc.types.Field(customer_obj_rel_insert_input, graphql_name='customer')
    role = sgqlc.types.Field(role_obj_rel_insert_input, graphql_name='role')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')


class roles_customers_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(roles_customers_insert_input), graphql_name='data')


class roles_customers_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('customer', 'role', 'role_id', 'user_id')
    customer = sgqlc.types.Field(customer_order_by, graphql_name='customer')
    role = sgqlc.types.Field(role_order_by, graphql_name='role')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')


class roles_customers_stddev_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_sum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_var_pop_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_var_samp_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class roles_customers_variance_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(order_by, graphql_name='role_id')
    user_id = sgqlc.types.Field(order_by, graphql_name='user_id')


class source_enum_aggregate_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('count', 'max', 'min')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('source_enum_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('source_enum_min_order_by', graphql_name='min')


class source_enum_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('source_enum_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('source_enum_on_conflict', graphql_name='on_conflict')


class source_enum_bool_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_and', '_not', '_or', 'id', 'invoices')
    _and = sgqlc.types.Field(sgqlc.types.list_of('source_enum_bool_exp'), graphql_name='_and')
    _not = sgqlc.types.Field('source_enum_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of('source_enum_bool_exp'), graphql_name='_or')
    id = sgqlc.types.Field(String_comparison_exp, graphql_name='id')
    invoices = sgqlc.types.Field(invoice_bool_exp, graphql_name='invoices')


class source_enum_enum_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_in', '_is_null', '_neq', '_nin')
    _eq = sgqlc.types.Field(source_enum_enum, graphql_name='_eq')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_enum)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _neq = sgqlc.types.Field(source_enum_enum, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_enum)), graphql_name='_nin')


class source_enum_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id', 'invoices')
    id = sgqlc.types.Field(String, graphql_name='id')
    invoices = sgqlc.types.Field(invoice_arr_rel_insert_input, graphql_name='invoices')


class source_enum_max_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class source_enum_min_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(order_by, graphql_name='id')


class source_enum_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(source_enum_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('source_enum_on_conflict', graphql_name='on_conflict')


class source_enum_on_conflict(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(source_enum_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(source_enum_bool_exp, graphql_name='where')


class source_enum_order_by(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id', 'invoices_aggregate')
    id = sgqlc.types.Field(order_by, graphql_name='id')
    invoices_aggregate = sgqlc.types.Field(invoice_aggregate_order_by, graphql_name='invoices_aggregate')


class source_enum_pk_columns_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class source_enum_set_input(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(String, graphql_name='id')


class timestamp_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(timestamp, graphql_name='_eq')
    _gt = sgqlc.types.Field(timestamp, graphql_name='_gt')
    _gte = sgqlc.types.Field(timestamp, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timestamp)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(timestamp, graphql_name='_lt')
    _lte = sgqlc.types.Field(timestamp, graphql_name='_lte')
    _neq = sgqlc.types.Field(timestamp, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timestamp)), graphql_name='_nin')


class timestamptz_comparison_exp(sgqlc.types.Input):
    __schema__ = schema_dev
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(timestamptz, graphql_name='_eq')
    _gt = sgqlc.types.Field(timestamptz, graphql_name='_gt')
    _gte = sgqlc.types.Field(timestamptz, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timestamptz)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(timestamptz, graphql_name='_lt')
    _lte = sgqlc.types.Field(timestamptz, graphql_name='_lte')
    _neq = sgqlc.types.Field(timestamptz, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timestamptz)), graphql_name='_nin')



########################################################################
# Output Objects and Interfaces
########################################################################
class company(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('address', 'bankruptcy', 'business_interruption', 'eb_session_infos', 'eb_session_infos_aggregate', 'forecast_events', 'forecast_events_aggregate', 'forecasts', 'forecasts_aggregate', 'founded_date', 'groups', 'groups_aggregate', 'id', 'industry', 'invoices_by_buyer', 'invoices_by_buyer_aggregate', 'invoices_by_seller', 'invoices_by_seller_aggregate', 'liquidation', 'name', 'netvisor_infos', 'netvisor_infos_aggregate', 'procountor_infos', 'procountor_infos_aggregate', 'restructuring', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(String, graphql_name='address')
    bankruptcy = sgqlc.types.Field(Boolean, graphql_name='bankruptcy')
    business_interruption = sgqlc.types.Field(Boolean, graphql_name='business_interruption')
    eb_session_infos = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_session_info'))), graphql_name='eb_session_infos', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_session_info_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_session_infos_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_session_info_aggregate'), graphql_name='eb_session_infos_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_session_info_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast_event'))), graphql_name='forecast_events', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_events_aggregate = sgqlc.types.Field(sgqlc.types.non_null('forecast_event_aggregate'), graphql_name='forecast_events_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    forecasts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast'))), graphql_name='forecasts', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_bool_exp, graphql_name='where', default=None)),
))
    )
    forecasts_aggregate = sgqlc.types.Field(sgqlc.types.non_null('forecast_aggregate'), graphql_name='forecasts_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_bool_exp, graphql_name='where', default=None)),
))
    )
    founded_date = sgqlc.types.Field(date, graphql_name='founded_date')
    groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group'))), graphql_name='groups', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_bool_exp, graphql_name='where', default=None)),
))
    )
    groups_aggregate = sgqlc.types.Field(sgqlc.types.non_null('group_aggregate'), graphql_name='groups_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_bool_exp, graphql_name='where', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    industry = sgqlc.types.Field(String, graphql_name='industry')
    invoices_by_buyer = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice'))), graphql_name='invoices_by_buyer', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoices_by_buyer_aggregate = sgqlc.types.Field(sgqlc.types.non_null('invoice_aggregate'), graphql_name='invoices_by_buyer_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoices_by_seller = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice'))), graphql_name='invoices_by_seller', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoices_by_seller_aggregate = sgqlc.types.Field(sgqlc.types.non_null('invoice_aggregate'), graphql_name='invoices_by_seller_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    liquidation = sgqlc.types.Field(Boolean, graphql_name='liquidation')
    name = sgqlc.types.Field(String, graphql_name='name')
    netvisor_infos = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('netvisor_info'))), graphql_name='netvisor_infos', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(netvisor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    netvisor_infos_aggregate = sgqlc.types.Field(sgqlc.types.non_null('netvisor_info_aggregate'), graphql_name='netvisor_infos_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(netvisor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    procountor_infos = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('procountor_info'))), graphql_name='procountor_infos', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(procountor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    procountor_infos_aggregate = sgqlc.types.Field(sgqlc.types.non_null('procountor_info_aggregate'), graphql_name='procountor_infos_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(procountor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    restructuring = sgqlc.types.Field(Boolean, graphql_name='restructuring')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    vat = sgqlc.types.Field(String, graphql_name='vat')


class company_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('company_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(company))), graphql_name='nodes')


class company_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('company_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('company_max_fields', graphql_name='max')
    min = sgqlc.types.Field('company_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('company_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('company_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('company_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('company_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('company_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('company_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('company_variance_fields', graphql_name='variance')


class company_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class company_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('address', 'founded_date', 'id', 'industry', 'name', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(String, graphql_name='address')
    founded_date = sgqlc.types.Field(date, graphql_name='founded_date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    industry = sgqlc.types.Field(String, graphql_name='industry')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    vat = sgqlc.types.Field(String, graphql_name='vat')


class company_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('address', 'founded_date', 'id', 'industry', 'name', 'time_created', 'time_updated', 'vat')
    address = sgqlc.types.Field(String, graphql_name='address')
    founded_date = sgqlc.types.Field(date, graphql_name='founded_date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    industry = sgqlc.types.Field(String, graphql_name='industry')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    vat = sgqlc.types.Field(String, graphql_name='vat')


class company_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(company))), graphql_name='returning')


class company_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class company_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class company_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class company_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Int, graphql_name='id')


class company_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class company_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class company_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class customer(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('email', 'email_subscription', 'group', 'group_id', 'id', 'password_hash', 'roles_customers', 'roles_customers_aggregate', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    email_subscription = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='email_subscription')
    group = sgqlc.types.Field('group', graphql_name='group')
    group_id = sgqlc.types.Field(Int, graphql_name='group_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    password_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password_hash')
    roles_customers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('roles_customers'))), graphql_name='roles_customers', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    roles_customers_aggregate = sgqlc.types.Field(sgqlc.types.non_null('roles_customers_aggregate'), graphql_name='roles_customers_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class customer_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('customer_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(customer))), graphql_name='nodes')


class customer_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('customer_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('customer_max_fields', graphql_name='max')
    min = sgqlc.types.Field('customer_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('customer_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('customer_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('customer_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('customer_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('customer_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('customer_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('customer_variance_fields', graphql_name='variance')


class customer_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Float, graphql_name='group_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class customer_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('email', 'group_id', 'id', 'password_hash', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(String, graphql_name='email')
    group_id = sgqlc.types.Field(Int, graphql_name='group_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    password_hash = sgqlc.types.Field(String, graphql_name='password_hash')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class customer_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('email', 'group_id', 'id', 'password_hash', 'status', 'time_created', 'time_updated')
    email = sgqlc.types.Field(String, graphql_name='email')
    group_id = sgqlc.types.Field(Int, graphql_name='group_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    password_hash = sgqlc.types.Field(String, graphql_name='password_hash')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class customer_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(customer))), graphql_name='returning')


class customer_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Float, graphql_name='group_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class customer_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Float, graphql_name='group_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class customer_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Float, graphql_name='group_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class customer_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Int, graphql_name='group_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class customer_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Float, graphql_name='group_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class customer_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Float, graphql_name='group_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class customer_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_id', 'id')
    group_id = sgqlc.types.Field(Float, graphql_name='group_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_balance(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='amount')
    balance_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='balance_type')
    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currency')
    eb_bank_account = sgqlc.types.Field(sgqlc.types.non_null('eb_bank_account'), graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    last_change_date_time = sgqlc.types.Field(timestamp, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(timestamp, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    reference_date = sgqlc.types.Field(date, graphql_name='reference_date')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_balance_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('eb_balance_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance))), graphql_name='nodes')


class eb_balance_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_balance_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('eb_balance_max_fields', graphql_name='max')
    min = sgqlc.types.Field('eb_balance_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('eb_balance_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_balance_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_balance_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_balance_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_balance_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_balance_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_balance_variance_fields', graphql_name='variance')


class eb_balance_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_balance_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    balance_type = sgqlc.types.Field(String, graphql_name='balance_type')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    last_change_date_time = sgqlc.types.Field(timestamp, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(timestamp, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(String, graphql_name='name')
    reference_date = sgqlc.types.Field(date, graphql_name='reference_date')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_balance_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'balance_type', 'currency', 'eb_bank_account_id', 'id', 'last_change_date_time', 'last_committed_transaction', 'name', 'reference_date', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    balance_type = sgqlc.types.Field(String, graphql_name='balance_type')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    last_change_date_time = sgqlc.types.Field(timestamp, graphql_name='last_change_date_time')
    last_committed_transaction = sgqlc.types.Field(timestamp, graphql_name='last_committed_transaction')
    name = sgqlc.types.Field(String, graphql_name='name')
    reference_date = sgqlc.types.Field(date, graphql_name='reference_date')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_balance_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance))), graphql_name='returning')


class eb_balance_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_balance_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_balance_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_balance_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_balance_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_balance_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_balance_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_bank_account(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_balances', 'eb_balances_aggregate', 'eb_session_info', 'eb_session_info_id', 'eb_transactions', 'eb_transactions_aggregate', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account_uid')
    eb_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance))), graphql_name='eb_balances', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_balance_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_balances_aggregate = sgqlc.types.Field(sgqlc.types.non_null(eb_balance_aggregate), graphql_name='eb_balances_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_balance_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_session_info = sgqlc.types.Field(sgqlc.types.non_null('eb_session_info'), graphql_name='eb_session_info')
    eb_session_info_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eb_session_info_id')
    eb_transactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_transaction'))), graphql_name='eb_transactions', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_transaction_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_transactions_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_transaction_aggregate'), graphql_name='eb_transactions_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_transaction_bool_exp, graphql_name='where', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    identification_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identification_hash')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_bank_account_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('eb_bank_account_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account))), graphql_name='nodes')


class eb_bank_account_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_bank_account_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('eb_bank_account_max_fields', graphql_name='max')
    min = sgqlc.types.Field('eb_bank_account_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('eb_bank_account_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_bank_account_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_bank_account_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_bank_account_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_bank_account_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_bank_account_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_bank_account_variance_fields', graphql_name='variance')


class eb_bank_account_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Float, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_bank_account_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_session_info_id', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(String, graphql_name='account_uid')
    eb_session_info_id = sgqlc.types.Field(Int, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    identification_hash = sgqlc.types.Field(String, graphql_name='identification_hash')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_bank_account_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('account_uid', 'eb_session_info_id', 'id', 'identification_hash', 'time_created', 'time_updated')
    account_uid = sgqlc.types.Field(String, graphql_name='account_uid')
    eb_session_info_id = sgqlc.types.Field(Int, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    identification_hash = sgqlc.types.Field(String, graphql_name='identification_hash')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_bank_account_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account))), graphql_name='returning')


class eb_bank_account_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Float, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_bank_account_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Float, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_bank_account_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Float, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_bank_account_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Int, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_bank_account_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Float, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_bank_account_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Float, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_bank_account_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('eb_session_info_id', 'id')
    eb_session_info_id = sgqlc.types.Field(Float, graphql_name='eb_session_info_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_keys(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    private_key = sgqlc.types.Field(String, graphql_name='private_key')
    public_cert = sgqlc.types.Field(String, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(String, graphql_name='public_pem')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_keys_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('eb_keys_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys))), graphql_name='nodes')


class eb_keys_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_keys_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('eb_keys_max_fields', graphql_name='max')
    min = sgqlc.types.Field('eb_keys_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('eb_keys_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_keys_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_keys_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_keys_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_keys_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_keys_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_keys_variance_fields', graphql_name='variance')


class eb_keys_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_keys_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(Int, graphql_name='id')
    private_key = sgqlc.types.Field(String, graphql_name='private_key')
    public_cert = sgqlc.types.Field(String, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(String, graphql_name='public_pem')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_keys_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id', 'private_key', 'public_cert', 'public_pem', 'time_created', 'time_updated')
    id = sgqlc.types.Field(Int, graphql_name='id')
    private_key = sgqlc.types.Field(String, graphql_name='private_key')
    public_cert = sgqlc.types.Field(String, graphql_name='public_cert')
    public_pem = sgqlc.types.Field(String, graphql_name='public_pem')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class eb_keys_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys))), graphql_name='returning')


class eb_keys_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_keys_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_keys_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_keys_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_keys_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_keys_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_keys_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_session_info(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'eb_bank_accounts', 'eb_bank_accounts_aggregate', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company = sgqlc.types.Field(sgqlc.types.non_null('company'), graphql_name='company')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='company_id')
    eb_bank_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account))), graphql_name='eb_bank_accounts', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_bank_account_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_bank_accounts_aggregate = sgqlc.types.Field(sgqlc.types.non_null(eb_bank_account_aggregate), graphql_name='eb_bank_accounts_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_bank_account_bool_exp, graphql_name='where', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    session_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='session_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(date, graphql_name='valid_until')


class eb_session_info_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('eb_session_info_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info))), graphql_name='nodes')


class eb_session_info_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_session_info_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('eb_session_info_max_fields', graphql_name='max')
    min = sgqlc.types.Field('eb_session_info_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('eb_session_info_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_session_info_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_session_info_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_session_info_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_session_info_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_session_info_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_session_info_variance_fields', graphql_name='variance')


class eb_session_info_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_session_info_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    session_id = sgqlc.types.Field(String, graphql_name='session_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(date, graphql_name='valid_until')


class eb_session_info_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'session_id', 'time_created', 'time_updated', 'valid_until')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    session_id = sgqlc.types.Field(String, graphql_name='session_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    valid_until = sgqlc.types.Field(date, graphql_name='valid_until')


class eb_session_info_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info))), graphql_name='returning')


class eb_session_info_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_session_info_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_session_info_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_session_info_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_session_info_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_session_info_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_session_info_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_transaction(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(String, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(date, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(String, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(String, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(String, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(String, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(String, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(String, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(String, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(String, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(String, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(String, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(String, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account = sgqlc.types.Field(sgqlc.types.non_null('eb_bank_account'), graphql_name='eb_bank_account')
    eb_bank_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(String, graphql_name='entry_reference')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    merchant_category_code = sgqlc.types.Field(String, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(String, graphql_name='remittance_information')
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(date, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(date, graphql_name='value_date')


class eb_transaction_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('eb_transaction_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction))), graphql_name='nodes')


class eb_transaction_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('eb_transaction_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('eb_transaction_max_fields', graphql_name='max')
    min = sgqlc.types.Field('eb_transaction_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('eb_transaction_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('eb_transaction_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('eb_transaction_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('eb_transaction_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('eb_transaction_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('eb_transaction_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('eb_transaction_variance_fields', graphql_name='variance')


class eb_transaction_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_transaction_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(String, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(date, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(String, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(String, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(String, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(String, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(String, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(String, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(String, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(String, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(String, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(String, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(String, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(String, graphql_name='entry_reference')
    id = sgqlc.types.Field(Int, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(String, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(String, graphql_name='remittance_information')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(date, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(date, graphql_name='value_date')


class eb_transaction_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'bank_transaction_code_code', 'bank_transaction_code_description', 'bank_transaction_code_sub_code', 'booking_date', 'credit_debit_indicator', 'creditor_account_iban', 'creditor_account_identification', 'creditor_account_issuer', 'creditor_account_scheme_name', 'creditor_name', 'creditor_organisation_id_identification', 'creditor_organisation_id_issuer', 'creditor_organisation_id_scheme_name', 'creditor_private_id_identification', 'creditor_private_id_issuer', 'creditor_private_id_scheme_name', 'currency', 'debtor_account_iban', 'debtor_account_identification', 'debtor_account_issuer', 'debtor_account_scheme_name', 'debtor_name', 'debtor_organisation_id_identification', 'debtor_organisation_id_issuer', 'debtor_organisation_id_scheme_name', 'debtor_private_id_identification', 'debtor_private_id_issuer', 'debtor_private_id_scheme_name', 'eb_bank_account_id', 'entry_reference', 'id', 'merchant_category_code', 'remittance_information', 'status', 'time_created', 'time_updated', 'transaction_date', 'value_date')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    bank_transaction_code_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_code')
    bank_transaction_code_description = sgqlc.types.Field(String, graphql_name='bank_transaction_code_description')
    bank_transaction_code_sub_code = sgqlc.types.Field(String, graphql_name='bank_transaction_code_sub_code')
    booking_date = sgqlc.types.Field(date, graphql_name='booking_date')
    credit_debit_indicator = sgqlc.types.Field(String, graphql_name='credit_debit_indicator')
    creditor_account_iban = sgqlc.types.Field(String, graphql_name='creditor_account_iban')
    creditor_account_identification = sgqlc.types.Field(String, graphql_name='creditor_account_identification')
    creditor_account_issuer = sgqlc.types.Field(String, graphql_name='creditor_account_issuer')
    creditor_account_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_account_scheme_name')
    creditor_name = sgqlc.types.Field(String, graphql_name='creditor_name')
    creditor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_identification')
    creditor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_issuer')
    creditor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_organisation_id_scheme_name')
    creditor_private_id_identification = sgqlc.types.Field(String, graphql_name='creditor_private_id_identification')
    creditor_private_id_issuer = sgqlc.types.Field(String, graphql_name='creditor_private_id_issuer')
    creditor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='creditor_private_id_scheme_name')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    debtor_account_iban = sgqlc.types.Field(String, graphql_name='debtor_account_iban')
    debtor_account_identification = sgqlc.types.Field(String, graphql_name='debtor_account_identification')
    debtor_account_issuer = sgqlc.types.Field(String, graphql_name='debtor_account_issuer')
    debtor_account_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_account_scheme_name')
    debtor_name = sgqlc.types.Field(String, graphql_name='debtor_name')
    debtor_organisation_id_identification = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_identification')
    debtor_organisation_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_issuer')
    debtor_organisation_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_organisation_id_scheme_name')
    debtor_private_id_identification = sgqlc.types.Field(String, graphql_name='debtor_private_id_identification')
    debtor_private_id_issuer = sgqlc.types.Field(String, graphql_name='debtor_private_id_issuer')
    debtor_private_id_scheme_name = sgqlc.types.Field(String, graphql_name='debtor_private_id_scheme_name')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    entry_reference = sgqlc.types.Field(String, graphql_name='entry_reference')
    id = sgqlc.types.Field(Int, graphql_name='id')
    merchant_category_code = sgqlc.types.Field(String, graphql_name='merchant_category_code')
    remittance_information = sgqlc.types.Field(String, graphql_name='remittance_information')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    transaction_date = sgqlc.types.Field(date, graphql_name='transaction_date')
    value_date = sgqlc.types.Field(date, graphql_name='value_date')


class eb_transaction_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction))), graphql_name='returning')


class eb_transaction_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_transaction_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_transaction_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_transaction_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Int, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class eb_transaction_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_transaction_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class eb_transaction_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'eb_bank_account_id', 'id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    eb_bank_account_id = sgqlc.types.Field(Float, graphql_name='eb_bank_account_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company = sgqlc.types.Field(sgqlc.types.non_null('company'), graphql_name='company')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='company_id')
    date = sgqlc.types.Field(sgqlc.types.non_null('date'), graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lower_bound = sgqlc.types.Field(float8, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8, graphql_name='median')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(float8, graphql_name='upper_bound')


class forecast_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('forecast_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast))), graphql_name='nodes')


class forecast_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('forecast_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('forecast_max_fields', graphql_name='max')
    min = sgqlc.types.Field('forecast_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('forecast_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('forecast_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('forecast_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('forecast_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('forecast_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('forecast_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('forecast_variance_fields', graphql_name='variance')


class forecast_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')
    lower_bound = sgqlc.types.Field(Float, graphql_name='lower_bound')
    median = sgqlc.types.Field(Float, graphql_name='median')
    upper_bound = sgqlc.types.Field(Float, graphql_name='upper_bound')


class forecast_event(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'data', 'event_class', 'id', 'invoice_type_enum', 'time_created', 'time_updated', 'type')
    company = sgqlc.types.Field('company', graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    data = sgqlc.types.Field(String, graphql_name='data')
    event_class = sgqlc.types.Field(String, graphql_name='event_class')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    invoice_type_enum = sgqlc.types.Field(sgqlc.types.non_null('invoice_type_enum'), graphql_name='invoice_type_enum')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    type = sgqlc.types.Field(sgqlc.types.non_null(invoice_type_enum_enum), graphql_name='type')


class forecast_event_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('forecast_event_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event))), graphql_name='nodes')


class forecast_event_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('forecast_event_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('forecast_event_max_fields', graphql_name='max')
    min = sgqlc.types.Field('forecast_event_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('forecast_event_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('forecast_event_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('forecast_event_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('forecast_event_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('forecast_event_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('forecast_event_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('forecast_event_variance_fields', graphql_name='variance')


class forecast_event_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast_event_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'data', 'event_class', 'id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    data = sgqlc.types.Field(String, graphql_name='data')
    event_class = sgqlc.types.Field(String, graphql_name='event_class')
    id = sgqlc.types.Field(Int, graphql_name='id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class forecast_event_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'data', 'event_class', 'id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    data = sgqlc.types.Field(String, graphql_name='data')
    event_class = sgqlc.types.Field(String, graphql_name='event_class')
    id = sgqlc.types.Field(Int, graphql_name='id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class forecast_event_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event))), graphql_name='returning')


class forecast_event_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast_event_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast_event_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast_event_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class forecast_event_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast_event_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast_event_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class forecast_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    date = sgqlc.types.Field('date', graphql_name='date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    lower_bound = sgqlc.types.Field(float8, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8, graphql_name='median')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(float8, graphql_name='upper_bound')


class forecast_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'date', 'id', 'lower_bound', 'median', 'time_created', 'time_updated', 'upper_bound')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    date = sgqlc.types.Field('date', graphql_name='date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    lower_bound = sgqlc.types.Field(float8, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8, graphql_name='median')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    upper_bound = sgqlc.types.Field(float8, graphql_name='upper_bound')


class forecast_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast))), graphql_name='returning')


class forecast_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')
    lower_bound = sgqlc.types.Field(Float, graphql_name='lower_bound')
    median = sgqlc.types.Field(Float, graphql_name='median')
    upper_bound = sgqlc.types.Field(Float, graphql_name='upper_bound')


class forecast_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')
    lower_bound = sgqlc.types.Field(Float, graphql_name='lower_bound')
    median = sgqlc.types.Field(Float, graphql_name='median')
    upper_bound = sgqlc.types.Field(Float, graphql_name='upper_bound')


class forecast_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')
    lower_bound = sgqlc.types.Field(Float, graphql_name='lower_bound')
    median = sgqlc.types.Field(Float, graphql_name='median')
    upper_bound = sgqlc.types.Field(Float, graphql_name='upper_bound')


class forecast_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    lower_bound = sgqlc.types.Field(float8, graphql_name='lower_bound')
    median = sgqlc.types.Field(float8, graphql_name='median')
    upper_bound = sgqlc.types.Field(float8, graphql_name='upper_bound')


class forecast_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')
    lower_bound = sgqlc.types.Field(Float, graphql_name='lower_bound')
    median = sgqlc.types.Field(Float, graphql_name='median')
    upper_bound = sgqlc.types.Field(Float, graphql_name='upper_bound')


class forecast_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')
    lower_bound = sgqlc.types.Field(Float, graphql_name='lower_bound')
    median = sgqlc.types.Field(Float, graphql_name='median')
    upper_bound = sgqlc.types.Field(Float, graphql_name='upper_bound')


class forecast_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'lower_bound', 'median', 'upper_bound')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')
    lower_bound = sgqlc.types.Field(Float, graphql_name='lower_bound')
    median = sgqlc.types.Field(Float, graphql_name='median')
    upper_bound = sgqlc.types.Field(Float, graphql_name='upper_bound')


class group(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'customers', 'customers_aggregate', 'group_relations_by_primary', 'group_relations_by_primary_aggregate', 'group_relations_by_secondary', 'group_relations_by_secondary_aggregate', 'id', 'name', 'time_created', 'time_updated')
    company = sgqlc.types.Field('company', graphql_name='company')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    customers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(customer))), graphql_name='customers', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(customer_bool_exp, graphql_name='where', default=None)),
))
    )
    customers_aggregate = sgqlc.types.Field(sgqlc.types.non_null(customer_aggregate), graphql_name='customers_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(customer_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relations_by_primary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group_relation'))), graphql_name='group_relations_by_primary', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relations_by_primary_aggregate = sgqlc.types.Field(sgqlc.types.non_null('group_relation_aggregate'), graphql_name='group_relations_by_primary_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relations_by_secondary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group_relation'))), graphql_name='group_relations_by_secondary', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relations_by_secondary_aggregate = sgqlc.types.Field(sgqlc.types.non_null('group_relation_aggregate'), graphql_name='group_relations_by_secondary_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class group_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('group_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group))), graphql_name='nodes')


class group_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('group_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('group_max_fields', graphql_name='max')
    min = sgqlc.types.Field('group_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('group_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('group_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('group_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('group_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('group_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('group_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('group_variance_fields', graphql_name='variance')


class group_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class group_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'name', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class group_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'name', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class group_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group))), graphql_name='returning')


class group_relation(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('group_by_primary', 'group_by_secondary', 'primary_id', 'secondary_id')
    group_by_primary = sgqlc.types.Field(sgqlc.types.non_null(group), graphql_name='group_by_primary')
    group_by_secondary = sgqlc.types.Field(sgqlc.types.non_null(group), graphql_name='group_by_secondary')
    primary_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='secondary_id')


class group_relation_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('group_relation_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group_relation))), graphql_name='nodes')


class group_relation_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('group_relation_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('group_relation_max_fields', graphql_name='max')
    min = sgqlc.types.Field('group_relation_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('group_relation_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('group_relation_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('group_relation_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('group_relation_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('group_relation_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('group_relation_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('group_relation_variance_fields', graphql_name='variance')


class group_relation_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Float, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Float, graphql_name='secondary_id')


class group_relation_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Int, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Int, graphql_name='secondary_id')


class group_relation_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Int, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Int, graphql_name='secondary_id')


class group_relation_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group_relation))), graphql_name='returning')


class group_relation_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Float, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Float, graphql_name='secondary_id')


class group_relation_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Float, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Float, graphql_name='secondary_id')


class group_relation_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Float, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Float, graphql_name='secondary_id')


class group_relation_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Int, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Int, graphql_name='secondary_id')


class group_relation_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Float, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Float, graphql_name='secondary_id')


class group_relation_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Float, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Float, graphql_name='secondary_id')


class group_relation_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('primary_id', 'secondary_id')
    primary_id = sgqlc.types.Field(Float, graphql_name='primary_id')
    secondary_id = sgqlc.types.Field(Float, graphql_name='secondary_id')


class group_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class group_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class group_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class group_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class group_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class group_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class group_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class invoice(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'invoice_type_enum', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'payments', 'payments_aggregate', 'provider_status', 'reference_number', 'seller', 'seller_id', 'source', 'source_enum', 'status', 'time_created', 'time_updated', 'type')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    buyer = sgqlc.types.Field(company, graphql_name='buyer')
    buyer_id = sgqlc.types.Field(Int, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(String, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(String, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(float8, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(date, graphql_name='create_date')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    currency_rate = sgqlc.types.Field(float8, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(date, graphql_name='due_date')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    invoice_type_enum = sgqlc.types.Field(sgqlc.types.non_null('invoice_type_enum'), graphql_name='invoice_type_enum')
    original_amount = sgqlc.types.Field(float8, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(float8, graphql_name='payment_term_percentage')
    payments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('payment'))), graphql_name='payments', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(payment_bool_exp, graphql_name='where', default=None)),
))
    )
    payments_aggregate = sgqlc.types.Field(sgqlc.types.non_null('payment_aggregate'), graphql_name='payments_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(payment_bool_exp, graphql_name='where', default=None)),
))
    )
    provider_status = sgqlc.types.Field(String, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reference_number')
    seller = sgqlc.types.Field(company, graphql_name='seller')
    seller_id = sgqlc.types.Field(Int, graphql_name='seller_id')
    source = sgqlc.types.Field(sgqlc.types.non_null(source_enum_enum), graphql_name='source')
    source_enum = sgqlc.types.Field(sgqlc.types.non_null('source_enum'), graphql_name='source_enum')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')
    type = sgqlc.types.Field(sgqlc.types.non_null(invoice_type_enum_enum), graphql_name='type')


class invoice_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('invoice_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice))), graphql_name='nodes')


class invoice_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('invoice_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('invoice_max_fields', graphql_name='max')
    min = sgqlc.types.Field('invoice_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('invoice_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('invoice_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('invoice_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('invoice_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('invoice_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('invoice_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('invoice_variance_fields', graphql_name='variance')


class invoice_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Float, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(Float, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(Float, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(Float, graphql_name='currency_rate')
    id = sgqlc.types.Field(Float, graphql_name='id')
    original_amount = sgqlc.types.Field(Float, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(Float, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(Float, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Float, graphql_name='seller_id')


class invoice_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'provider_status', 'reference_number', 'seller_id', 'status', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Int, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(String, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(String, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(float8, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(date, graphql_name='create_date')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    currency_rate = sgqlc.types.Field(float8, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(date, graphql_name='due_date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    original_amount = sgqlc.types.Field(float8, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(float8, graphql_name='payment_term_percentage')
    provider_status = sgqlc.types.Field(String, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    seller_id = sgqlc.types.Field(Int, graphql_name='seller_id')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class invoice_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'buyer_name', 'buyer_vat', 'cash_discount_percentage', 'cash_discount_term', 'create_date', 'currency', 'currency_rate', 'due_date', 'id', 'original_amount', 'payed_amount', 'payment_date', 'payment_term_percentage', 'provider_status', 'reference_number', 'seller_id', 'status', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Int, graphql_name='buyer_id')
    buyer_name = sgqlc.types.Field(String, graphql_name='buyer_name')
    buyer_vat = sgqlc.types.Field(String, graphql_name='buyer_vat')
    cash_discount_percentage = sgqlc.types.Field(float8, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8, graphql_name='cash_discount_term')
    create_date = sgqlc.types.Field(date, graphql_name='create_date')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    currency_rate = sgqlc.types.Field(float8, graphql_name='currency_rate')
    due_date = sgqlc.types.Field(date, graphql_name='due_date')
    id = sgqlc.types.Field(Int, graphql_name='id')
    original_amount = sgqlc.types.Field(float8, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8, graphql_name='payed_amount')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    payment_term_percentage = sgqlc.types.Field(float8, graphql_name='payment_term_percentage')
    provider_status = sgqlc.types.Field(String, graphql_name='provider_status')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    seller_id = sgqlc.types.Field(Int, graphql_name='seller_id')
    status = sgqlc.types.Field(String, graphql_name='status')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class invoice_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice))), graphql_name='returning')


class invoice_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Float, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(Float, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(Float, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(Float, graphql_name='currency_rate')
    id = sgqlc.types.Field(Float, graphql_name='id')
    original_amount = sgqlc.types.Field(Float, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(Float, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(Float, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Float, graphql_name='seller_id')


class invoice_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Float, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(Float, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(Float, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(Float, graphql_name='currency_rate')
    id = sgqlc.types.Field(Float, graphql_name='id')
    original_amount = sgqlc.types.Field(Float, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(Float, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(Float, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Float, graphql_name='seller_id')


class invoice_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Float, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(Float, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(Float, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(Float, graphql_name='currency_rate')
    id = sgqlc.types.Field(Float, graphql_name='id')
    original_amount = sgqlc.types.Field(Float, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(Float, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(Float, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Float, graphql_name='seller_id')


class invoice_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Int, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(float8, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(float8, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(float8, graphql_name='currency_rate')
    id = sgqlc.types.Field(Int, graphql_name='id')
    original_amount = sgqlc.types.Field(float8, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(float8, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(float8, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Int, graphql_name='seller_id')


class invoice_type_enum(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('forecast_events', 'forecast_events_aggregate', 'id', 'invoices', 'invoices_aggregate')
    forecast_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event))), graphql_name='forecast_events', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_events_aggregate = sgqlc.types.Field(sgqlc.types.non_null(forecast_event_aggregate), graphql_name='forecast_events_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    invoices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice))), graphql_name='invoices', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoices_aggregate = sgqlc.types.Field(sgqlc.types.non_null(invoice_aggregate), graphql_name='invoices_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )


class invoice_type_enum_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('invoice_type_enum_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum))), graphql_name='nodes')


class invoice_type_enum_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('count', 'max', 'min')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('invoice_type_enum_max_fields', graphql_name='max')
    min = sgqlc.types.Field('invoice_type_enum_min_fields', graphql_name='min')


class invoice_type_enum_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(String, graphql_name='id')


class invoice_type_enum_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(String, graphql_name='id')


class invoice_type_enum_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum))), graphql_name='returning')


class invoice_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Float, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(Float, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(Float, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(Float, graphql_name='currency_rate')
    id = sgqlc.types.Field(Float, graphql_name='id')
    original_amount = sgqlc.types.Field(Float, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(Float, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(Float, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Float, graphql_name='seller_id')


class invoice_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Float, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(Float, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(Float, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(Float, graphql_name='currency_rate')
    id = sgqlc.types.Field(Float, graphql_name='id')
    original_amount = sgqlc.types.Field(Float, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(Float, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(Float, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Float, graphql_name='seller_id')


class invoice_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'buyer_id', 'cash_discount_percentage', 'cash_discount_term', 'currency_rate', 'id', 'original_amount', 'payed_amount', 'payment_term_percentage', 'seller_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    buyer_id = sgqlc.types.Field(Float, graphql_name='buyer_id')
    cash_discount_percentage = sgqlc.types.Field(Float, graphql_name='cash_discount_percentage')
    cash_discount_term = sgqlc.types.Field(Float, graphql_name='cash_discount_term')
    currency_rate = sgqlc.types.Field(Float, graphql_name='currency_rate')
    id = sgqlc.types.Field(Float, graphql_name='id')
    original_amount = sgqlc.types.Field(Float, graphql_name='original_amount')
    payed_amount = sgqlc.types.Field(Float, graphql_name='payed_amount')
    payment_term_percentage = sgqlc.types.Field(Float, graphql_name='payment_term_percentage')
    seller_id = sgqlc.types.Field(Float, graphql_name='seller_id')


class mutation_root(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('delete_company', 'delete_company_by_pk', 'delete_customer', 'delete_customer_by_pk', 'delete_eb_balance', 'delete_eb_balance_by_pk', 'delete_eb_bank_account', 'delete_eb_bank_account_by_pk', 'delete_eb_keys', 'delete_eb_keys_by_pk', 'delete_eb_session_info', 'delete_eb_session_info_by_pk', 'delete_eb_transaction', 'delete_eb_transaction_by_pk', 'delete_forecast', 'delete_forecast_by_pk', 'delete_forecast_event', 'delete_forecast_event_by_pk', 'delete_group', 'delete_group_by_pk', 'delete_group_relation', 'delete_group_relation_by_pk', 'delete_invoice', 'delete_invoice_by_pk', 'delete_invoice_type_enum', 'delete_invoice_type_enum_by_pk', 'delete_netvisor_info', 'delete_netvisor_info_by_pk', 'delete_payment', 'delete_payment_by_pk', 'delete_procountor_info', 'delete_procountor_info_by_pk', 'delete_role', 'delete_role_by_pk', 'delete_roles_customers', 'delete_source_enum', 'delete_source_enum_by_pk', 'insert_company', 'insert_company_one', 'insert_customer', 'insert_customer_one', 'insert_eb_balance', 'insert_eb_balance_one', 'insert_eb_bank_account', 'insert_eb_bank_account_one', 'insert_eb_keys', 'insert_eb_keys_one', 'insert_eb_session_info', 'insert_eb_session_info_one', 'insert_eb_transaction', 'insert_eb_transaction_one', 'insert_forecast', 'insert_forecast_event', 'insert_forecast_event_one', 'insert_forecast_one', 'insert_group', 'insert_group_one', 'insert_group_relation', 'insert_group_relation_one', 'insert_invoice', 'insert_invoice_one', 'insert_invoice_type_enum', 'insert_invoice_type_enum_one', 'insert_netvisor_info', 'insert_netvisor_info_one', 'insert_payment', 'insert_payment_one', 'insert_procountor_info', 'insert_procountor_info_one', 'insert_role', 'insert_role_one', 'insert_roles_customers', 'insert_roles_customers_one', 'insert_source_enum', 'insert_source_enum_one', 'update_company', 'update_company_by_pk', 'update_customer', 'update_customer_by_pk', 'update_eb_balance', 'update_eb_balance_by_pk', 'update_eb_bank_account', 'update_eb_bank_account_by_pk', 'update_eb_keys', 'update_eb_keys_by_pk', 'update_eb_session_info', 'update_eb_session_info_by_pk', 'update_eb_transaction', 'update_eb_transaction_by_pk', 'update_forecast', 'update_forecast_by_pk', 'update_forecast_event', 'update_forecast_event_by_pk', 'update_group', 'update_group_by_pk', 'update_group_relation', 'update_group_relation_by_pk', 'update_invoice', 'update_invoice_by_pk', 'update_invoice_type_enum', 'update_invoice_type_enum_by_pk', 'update_netvisor_info', 'update_netvisor_info_by_pk', 'update_payment', 'update_payment_by_pk', 'update_procountor_info', 'update_procountor_info_by_pk', 'update_role', 'update_role_by_pk', 'update_roles_customers', 'update_source_enum', 'update_source_enum_by_pk')
    delete_company = sgqlc.types.Field(company_mutation_response, graphql_name='delete_company', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(company_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_company_by_pk = sgqlc.types.Field(company, graphql_name='delete_company_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_customer = sgqlc.types.Field(customer_mutation_response, graphql_name='delete_customer', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(customer_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_customer_by_pk = sgqlc.types.Field(customer, graphql_name='delete_customer_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_eb_balance = sgqlc.types.Field(eb_balance_mutation_response, graphql_name='delete_eb_balance', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_balance_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_eb_balance_by_pk = sgqlc.types.Field(eb_balance, graphql_name='delete_eb_balance_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_eb_bank_account = sgqlc.types.Field(eb_bank_account_mutation_response, graphql_name='delete_eb_bank_account', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_bank_account_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_eb_bank_account_by_pk = sgqlc.types.Field(eb_bank_account, graphql_name='delete_eb_bank_account_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_eb_keys = sgqlc.types.Field(eb_keys_mutation_response, graphql_name='delete_eb_keys', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_keys_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_eb_keys_by_pk = sgqlc.types.Field(eb_keys, graphql_name='delete_eb_keys_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_eb_session_info = sgqlc.types.Field(eb_session_info_mutation_response, graphql_name='delete_eb_session_info', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_session_info_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_eb_session_info_by_pk = sgqlc.types.Field(eb_session_info, graphql_name='delete_eb_session_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_eb_transaction = sgqlc.types.Field(eb_transaction_mutation_response, graphql_name='delete_eb_transaction', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_transaction_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_eb_transaction_by_pk = sgqlc.types.Field(eb_transaction, graphql_name='delete_eb_transaction_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_forecast = sgqlc.types.Field(forecast_mutation_response, graphql_name='delete_forecast', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(forecast_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_forecast_by_pk = sgqlc.types.Field(forecast, graphql_name='delete_forecast_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_forecast_event = sgqlc.types.Field(forecast_event_mutation_response, graphql_name='delete_forecast_event', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(forecast_event_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_forecast_event_by_pk = sgqlc.types.Field(forecast_event, graphql_name='delete_forecast_event_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_group = sgqlc.types.Field(group_mutation_response, graphql_name='delete_group', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(group_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_group_by_pk = sgqlc.types.Field(group, graphql_name='delete_group_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_group_relation = sgqlc.types.Field(group_relation_mutation_response, graphql_name='delete_group_relation', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(group_relation_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_group_relation_by_pk = sgqlc.types.Field(group_relation, graphql_name='delete_group_relation_by_pk', args=sgqlc.types.ArgDict((
        ('primary_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='primary_id', default=None)),
        ('secondary_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='secondary_id', default=None)),
))
    )
    delete_invoice = sgqlc.types.Field(invoice_mutation_response, graphql_name='delete_invoice', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(invoice_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_invoice_by_pk = sgqlc.types.Field(invoice, graphql_name='delete_invoice_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_invoice_type_enum = sgqlc.types.Field(invoice_type_enum_mutation_response, graphql_name='delete_invoice_type_enum', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(invoice_type_enum_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_invoice_type_enum_by_pk = sgqlc.types.Field(invoice_type_enum, graphql_name='delete_invoice_type_enum_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_netvisor_info = sgqlc.types.Field('netvisor_info_mutation_response', graphql_name='delete_netvisor_info', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(netvisor_info_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_netvisor_info_by_pk = sgqlc.types.Field('netvisor_info', graphql_name='delete_netvisor_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_payment = sgqlc.types.Field('payment_mutation_response', graphql_name='delete_payment', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(payment_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_payment_by_pk = sgqlc.types.Field('payment', graphql_name='delete_payment_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_procountor_info = sgqlc.types.Field('procountor_info_mutation_response', graphql_name='delete_procountor_info', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(procountor_info_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_procountor_info_by_pk = sgqlc.types.Field('procountor_info', graphql_name='delete_procountor_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_role = sgqlc.types.Field('role_mutation_response', graphql_name='delete_role', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(role_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_role_by_pk = sgqlc.types.Field('role', graphql_name='delete_role_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_roles_customers = sgqlc.types.Field('roles_customers_mutation_response', graphql_name='delete_roles_customers', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(roles_customers_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_source_enum = sgqlc.types.Field('source_enum_mutation_response', graphql_name='delete_source_enum', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(source_enum_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_source_enum_by_pk = sgqlc.types.Field('source_enum', graphql_name='delete_source_enum_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    insert_company = sgqlc.types.Field(company_mutation_response, graphql_name='insert_company', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(company_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(company_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_company_one = sgqlc.types.Field(company, graphql_name='insert_company_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(company_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(company_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_customer = sgqlc.types.Field(customer_mutation_response, graphql_name='insert_customer', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(customer_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(customer_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_customer_one = sgqlc.types.Field(customer, graphql_name='insert_customer_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(customer_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(customer_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_balance = sgqlc.types.Field(eb_balance_mutation_response, graphql_name='insert_eb_balance', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_balance_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_balance_one = sgqlc.types.Field(eb_balance, graphql_name='insert_eb_balance_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(eb_balance_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_balance_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_bank_account = sgqlc.types.Field(eb_bank_account_mutation_response, graphql_name='insert_eb_bank_account', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_bank_account_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_bank_account_one = sgqlc.types.Field(eb_bank_account, graphql_name='insert_eb_bank_account_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(eb_bank_account_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_bank_account_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_keys = sgqlc.types.Field(eb_keys_mutation_response, graphql_name='insert_eb_keys', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_keys_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_keys_one = sgqlc.types.Field(eb_keys, graphql_name='insert_eb_keys_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(eb_keys_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_keys_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_session_info = sgqlc.types.Field(eb_session_info_mutation_response, graphql_name='insert_eb_session_info', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_session_info_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_session_info_one = sgqlc.types.Field(eb_session_info, graphql_name='insert_eb_session_info_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(eb_session_info_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_session_info_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_transaction = sgqlc.types.Field(eb_transaction_mutation_response, graphql_name='insert_eb_transaction', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_transaction_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_eb_transaction_one = sgqlc.types.Field(eb_transaction, graphql_name='insert_eb_transaction_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(eb_transaction_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(eb_transaction_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_forecast = sgqlc.types.Field(forecast_mutation_response, graphql_name='insert_forecast', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(forecast_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_forecast_event = sgqlc.types.Field(forecast_event_mutation_response, graphql_name='insert_forecast_event', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(forecast_event_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_forecast_event_one = sgqlc.types.Field(forecast_event, graphql_name='insert_forecast_event_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(forecast_event_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(forecast_event_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_forecast_one = sgqlc.types.Field(forecast, graphql_name='insert_forecast_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(forecast_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(forecast_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_group = sgqlc.types.Field(group_mutation_response, graphql_name='insert_group', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(group_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_group_one = sgqlc.types.Field(group, graphql_name='insert_group_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(group_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(group_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_group_relation = sgqlc.types.Field(group_relation_mutation_response, graphql_name='insert_group_relation', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(group_relation_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_group_relation_one = sgqlc.types.Field(group_relation, graphql_name='insert_group_relation_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(group_relation_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(group_relation_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_invoice = sgqlc.types.Field(invoice_mutation_response, graphql_name='insert_invoice', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(invoice_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_invoice_one = sgqlc.types.Field(invoice, graphql_name='insert_invoice_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(invoice_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(invoice_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_invoice_type_enum = sgqlc.types.Field(invoice_type_enum_mutation_response, graphql_name='insert_invoice_type_enum', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(invoice_type_enum_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_invoice_type_enum_one = sgqlc.types.Field(invoice_type_enum, graphql_name='insert_invoice_type_enum_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(invoice_type_enum_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(invoice_type_enum_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_netvisor_info = sgqlc.types.Field('netvisor_info_mutation_response', graphql_name='insert_netvisor_info', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(netvisor_info_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_netvisor_info_one = sgqlc.types.Field('netvisor_info', graphql_name='insert_netvisor_info_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(netvisor_info_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(netvisor_info_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_payment = sgqlc.types.Field('payment_mutation_response', graphql_name='insert_payment', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(payment_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(payment_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_payment_one = sgqlc.types.Field('payment', graphql_name='insert_payment_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(payment_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(payment_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_procountor_info = sgqlc.types.Field('procountor_info_mutation_response', graphql_name='insert_procountor_info', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(procountor_info_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_procountor_info_one = sgqlc.types.Field('procountor_info', graphql_name='insert_procountor_info_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(procountor_info_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(procountor_info_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_role = sgqlc.types.Field('role_mutation_response', graphql_name='insert_role', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(role_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(role_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_role_one = sgqlc.types.Field('role', graphql_name='insert_role_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(role_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(role_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_roles_customers = sgqlc.types.Field('roles_customers_mutation_response', graphql_name='insert_roles_customers', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_insert_input))), graphql_name='objects', default=None)),
))
    )
    insert_roles_customers_one = sgqlc.types.Field('roles_customers', graphql_name='insert_roles_customers_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(roles_customers_insert_input), graphql_name='object', default=None)),
))
    )
    insert_source_enum = sgqlc.types.Field('source_enum_mutation_response', graphql_name='insert_source_enum', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(source_enum_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_source_enum_one = sgqlc.types.Field('source_enum', graphql_name='insert_source_enum_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(source_enum_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(source_enum_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    update_company = sgqlc.types.Field(company_mutation_response, graphql_name='update_company', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(company_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(company_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(company_bool_exp), graphql_name='where', default=None)),
))
    )
    update_company_by_pk = sgqlc.types.Field(company, graphql_name='update_company_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(company_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(company_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(company_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_customer = sgqlc.types.Field(customer_mutation_response, graphql_name='update_customer', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(customer_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(customer_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(customer_bool_exp), graphql_name='where', default=None)),
))
    )
    update_customer_by_pk = sgqlc.types.Field(customer, graphql_name='update_customer_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(customer_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(customer_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(customer_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_eb_balance = sgqlc.types.Field(eb_balance_mutation_response, graphql_name='update_eb_balance', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_balance_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_balance_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_balance_bool_exp), graphql_name='where', default=None)),
))
    )
    update_eb_balance_by_pk = sgqlc.types.Field(eb_balance, graphql_name='update_eb_balance_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_balance_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_balance_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(eb_balance_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_eb_bank_account = sgqlc.types.Field(eb_bank_account_mutation_response, graphql_name='update_eb_bank_account', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_bank_account_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_bank_account_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_bank_account_bool_exp), graphql_name='where', default=None)),
))
    )
    update_eb_bank_account_by_pk = sgqlc.types.Field(eb_bank_account, graphql_name='update_eb_bank_account_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_bank_account_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_bank_account_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(eb_bank_account_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_eb_keys = sgqlc.types.Field(eb_keys_mutation_response, graphql_name='update_eb_keys', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_keys_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_keys_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_keys_bool_exp), graphql_name='where', default=None)),
))
    )
    update_eb_keys_by_pk = sgqlc.types.Field(eb_keys, graphql_name='update_eb_keys_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_keys_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_keys_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(eb_keys_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_eb_session_info = sgqlc.types.Field(eb_session_info_mutation_response, graphql_name='update_eb_session_info', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_session_info_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_session_info_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_session_info_bool_exp), graphql_name='where', default=None)),
))
    )
    update_eb_session_info_by_pk = sgqlc.types.Field(eb_session_info, graphql_name='update_eb_session_info_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_session_info_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_session_info_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(eb_session_info_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_eb_transaction = sgqlc.types.Field(eb_transaction_mutation_response, graphql_name='update_eb_transaction', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_transaction_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_transaction_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(eb_transaction_bool_exp), graphql_name='where', default=None)),
))
    )
    update_eb_transaction_by_pk = sgqlc.types.Field(eb_transaction, graphql_name='update_eb_transaction_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(eb_transaction_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(eb_transaction_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(eb_transaction_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_forecast = sgqlc.types.Field(forecast_mutation_response, graphql_name='update_forecast', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(forecast_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(forecast_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(forecast_bool_exp), graphql_name='where', default=None)),
))
    )
    update_forecast_by_pk = sgqlc.types.Field(forecast, graphql_name='update_forecast_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(forecast_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(forecast_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(forecast_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_forecast_event = sgqlc.types.Field(forecast_event_mutation_response, graphql_name='update_forecast_event', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(forecast_event_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(forecast_event_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(forecast_event_bool_exp), graphql_name='where', default=None)),
))
    )
    update_forecast_event_by_pk = sgqlc.types.Field(forecast_event, graphql_name='update_forecast_event_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(forecast_event_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(forecast_event_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(forecast_event_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_group = sgqlc.types.Field(group_mutation_response, graphql_name='update_group', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(group_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(group_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(group_bool_exp), graphql_name='where', default=None)),
))
    )
    update_group_by_pk = sgqlc.types.Field(group, graphql_name='update_group_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(group_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(group_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(group_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_group_relation = sgqlc.types.Field(group_relation_mutation_response, graphql_name='update_group_relation', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(group_relation_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(group_relation_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(group_relation_bool_exp), graphql_name='where', default=None)),
))
    )
    update_group_relation_by_pk = sgqlc.types.Field(group_relation, graphql_name='update_group_relation_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(group_relation_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(group_relation_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(group_relation_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_invoice = sgqlc.types.Field(invoice_mutation_response, graphql_name='update_invoice', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(invoice_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(invoice_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(invoice_bool_exp), graphql_name='where', default=None)),
))
    )
    update_invoice_by_pk = sgqlc.types.Field(invoice, graphql_name='update_invoice_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(invoice_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(invoice_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(invoice_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_invoice_type_enum = sgqlc.types.Field(invoice_type_enum_mutation_response, graphql_name='update_invoice_type_enum', args=sgqlc.types.ArgDict((
        ('_set', sgqlc.types.Arg(invoice_type_enum_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(invoice_type_enum_bool_exp), graphql_name='where', default=None)),
))
    )
    update_invoice_type_enum_by_pk = sgqlc.types.Field(invoice_type_enum, graphql_name='update_invoice_type_enum_by_pk', args=sgqlc.types.ArgDict((
        ('_set', sgqlc.types.Arg(invoice_type_enum_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(invoice_type_enum_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_netvisor_info = sgqlc.types.Field('netvisor_info_mutation_response', graphql_name='update_netvisor_info', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(netvisor_info_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(netvisor_info_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(netvisor_info_bool_exp), graphql_name='where', default=None)),
))
    )
    update_netvisor_info_by_pk = sgqlc.types.Field('netvisor_info', graphql_name='update_netvisor_info_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(netvisor_info_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(netvisor_info_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(netvisor_info_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_payment = sgqlc.types.Field('payment_mutation_response', graphql_name='update_payment', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(payment_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(payment_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(payment_bool_exp), graphql_name='where', default=None)),
))
    )
    update_payment_by_pk = sgqlc.types.Field('payment', graphql_name='update_payment_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(payment_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(payment_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(payment_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_procountor_info = sgqlc.types.Field('procountor_info_mutation_response', graphql_name='update_procountor_info', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(procountor_info_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(procountor_info_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(procountor_info_bool_exp), graphql_name='where', default=None)),
))
    )
    update_procountor_info_by_pk = sgqlc.types.Field('procountor_info', graphql_name='update_procountor_info_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(procountor_info_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(procountor_info_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(procountor_info_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_role = sgqlc.types.Field('role_mutation_response', graphql_name='update_role', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(role_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(role_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(role_bool_exp), graphql_name='where', default=None)),
))
    )
    update_role_by_pk = sgqlc.types.Field('role', graphql_name='update_role_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(role_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(role_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(role_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_roles_customers = sgqlc.types.Field('roles_customers_mutation_response', graphql_name='update_roles_customers', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(roles_customers_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(roles_customers_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(roles_customers_bool_exp), graphql_name='where', default=None)),
))
    )
    update_source_enum = sgqlc.types.Field('source_enum_mutation_response', graphql_name='update_source_enum', args=sgqlc.types.ArgDict((
        ('_set', sgqlc.types.Arg(source_enum_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(source_enum_bool_exp), graphql_name='where', default=None)),
))
    )
    update_source_enum_by_pk = sgqlc.types.Field('source_enum', graphql_name='update_source_enum_by_pk', args=sgqlc.types.ArgDict((
        ('_set', sgqlc.types.Arg(source_enum_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(source_enum_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )


class netvisor_info(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'id', 'is_active', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company = sgqlc.types.Field(sgqlc.types.non_null('company'), graphql_name='company')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='company_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')
    netvisor_customer_id = sgqlc.types.Field(String, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(String, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(String, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class netvisor_info_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('netvisor_info_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info))), graphql_name='nodes')


class netvisor_info_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('netvisor_info_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('netvisor_info_max_fields', graphql_name='max')
    min = sgqlc.types.Field('netvisor_info_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('netvisor_info_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('netvisor_info_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('netvisor_info_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('netvisor_info_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('netvisor_info_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('netvisor_info_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('netvisor_info_variance_fields', graphql_name='variance')


class netvisor_info_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class netvisor_info_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    netvisor_customer_id = sgqlc.types.Field(String, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(String, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(String, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class netvisor_info_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'netvisor_customer_id', 'netvisor_customer_key', 'netvisor_organization_id', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    netvisor_customer_id = sgqlc.types.Field(String, graphql_name='netvisor_customer_id')
    netvisor_customer_key = sgqlc.types.Field(String, graphql_name='netvisor_customer_key')
    netvisor_organization_id = sgqlc.types.Field(String, graphql_name='netvisor_organization_id')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class netvisor_info_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info))), graphql_name='returning')


class netvisor_info_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class netvisor_info_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class netvisor_info_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class netvisor_info_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class netvisor_info_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class netvisor_info_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class netvisor_info_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class payment(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    invoice = sgqlc.types.Field('invoice', graphql_name='invoice')
    invoice_id = sgqlc.types.Field(Int, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class payment_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('payment_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(payment))), graphql_name='nodes')


class payment_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('payment_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('payment_max_fields', graphql_name='max')
    min = sgqlc.types.Field('payment_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('payment_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('payment_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('payment_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('payment_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('payment_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('payment_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('payment_variance_fields', graphql_name='variance')


class payment_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    id = sgqlc.types.Field(Float, graphql_name='id')
    invoice_id = sgqlc.types.Field(Float, graphql_name='invoice_id')


class payment_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice_id = sgqlc.types.Field(Int, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class payment_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id', 'payment_date', 'reference_number', 'time_created', 'time_updated')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice_id = sgqlc.types.Field(Int, graphql_name='invoice_id')
    payment_date = sgqlc.types.Field(date, graphql_name='payment_date')
    reference_number = sgqlc.types.Field(String, graphql_name='reference_number')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class payment_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(payment))), graphql_name='returning')


class payment_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    id = sgqlc.types.Field(Float, graphql_name='id')
    invoice_id = sgqlc.types.Field(Float, graphql_name='invoice_id')


class payment_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    id = sgqlc.types.Field(Float, graphql_name='id')
    invoice_id = sgqlc.types.Field(Float, graphql_name='invoice_id')


class payment_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    id = sgqlc.types.Field(Float, graphql_name='id')
    invoice_id = sgqlc.types.Field(Float, graphql_name='invoice_id')


class payment_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(float8, graphql_name='amount')
    id = sgqlc.types.Field(Int, graphql_name='id')
    invoice_id = sgqlc.types.Field(Int, graphql_name='invoice_id')


class payment_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    id = sgqlc.types.Field(Float, graphql_name='id')
    invoice_id = sgqlc.types.Field(Float, graphql_name='invoice_id')


class payment_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    id = sgqlc.types.Field(Float, graphql_name='id')
    invoice_id = sgqlc.types.Field(Float, graphql_name='invoice_id')


class payment_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('amount', 'id', 'invoice_id')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    id = sgqlc.types.Field(Float, graphql_name='id')
    invoice_id = sgqlc.types.Field(Float, graphql_name='invoice_id')


class procountor_info(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_id', 'id', 'is_active', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company = sgqlc.types.Field(sgqlc.types.non_null('company'), graphql_name='company')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='company_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')
    procountor_refresh_token = sgqlc.types.Field(String, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(String, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class procountor_info_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('procountor_info_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info))), graphql_name='nodes')


class procountor_info_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('procountor_info_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('procountor_info_max_fields', graphql_name='max')
    min = sgqlc.types.Field('procountor_info_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('procountor_info_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('procountor_info_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('procountor_info_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('procountor_info_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('procountor_info_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('procountor_info_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('procountor_info_variance_fields', graphql_name='variance')


class procountor_info_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class procountor_info_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    procountor_refresh_token = sgqlc.types.Field(String, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(String, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class procountor_info_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id', 'procountor_refresh_token', 'procountor_token', 'time_created', 'time_updated')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    procountor_refresh_token = sgqlc.types.Field(String, graphql_name='procountor_refresh_token')
    procountor_token = sgqlc.types.Field(String, graphql_name='procountor_token')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class procountor_info_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info))), graphql_name='returning')


class procountor_info_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class procountor_info_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class procountor_info_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class procountor_info_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Int, graphql_name='company_id')
    id = sgqlc.types.Field(Int, graphql_name='id')


class procountor_info_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class procountor_info_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class procountor_info_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company_id', 'id')
    company_id = sgqlc.types.Field(Float, graphql_name='company_id')
    id = sgqlc.types.Field(Float, graphql_name='id')


class query_root(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_aggregate', 'company_by_pk', 'customer', 'customer_aggregate', 'customer_by_pk', 'eb_balance', 'eb_balance_aggregate', 'eb_balance_by_pk', 'eb_bank_account', 'eb_bank_account_aggregate', 'eb_bank_account_by_pk', 'eb_keys', 'eb_keys_aggregate', 'eb_keys_by_pk', 'eb_session_info', 'eb_session_info_aggregate', 'eb_session_info_by_pk', 'eb_transaction', 'eb_transaction_aggregate', 'eb_transaction_by_pk', 'forecast', 'forecast_aggregate', 'forecast_by_pk', 'forecast_event', 'forecast_event_aggregate', 'forecast_event_by_pk', 'group', 'group_aggregate', 'group_by_pk', 'group_relation', 'group_relation_aggregate', 'group_relation_by_pk', 'invoice', 'invoice_aggregate', 'invoice_by_pk', 'invoice_type_enum', 'invoice_type_enum_aggregate', 'invoice_type_enum_by_pk', 'netvisor_info', 'netvisor_info_aggregate', 'netvisor_info_by_pk', 'payment', 'payment_aggregate', 'payment_by_pk', 'procountor_info', 'procountor_info_aggregate', 'procountor_info_by_pk', 'role', 'role_aggregate', 'role_by_pk', 'roles_customers', 'roles_customers_aggregate', 'source_enum', 'source_enum_aggregate', 'source_enum_by_pk')
    company = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('company'))), graphql_name='company', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(company_bool_exp, graphql_name='where', default=None)),
))
    )
    company_aggregate = sgqlc.types.Field(sgqlc.types.non_null('company_aggregate'), graphql_name='company_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(company_bool_exp, graphql_name='where', default=None)),
))
    )
    company_by_pk = sgqlc.types.Field('company', graphql_name='company_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    customer = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('customer'))), graphql_name='customer', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(customer_bool_exp, graphql_name='where', default=None)),
))
    )
    customer_aggregate = sgqlc.types.Field(sgqlc.types.non_null('customer_aggregate'), graphql_name='customer_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(customer_bool_exp, graphql_name='where', default=None)),
))
    )
    customer_by_pk = sgqlc.types.Field('customer', graphql_name='customer_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_balance = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_balance'))), graphql_name='eb_balance', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_balance_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_balance_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_balance_aggregate'), graphql_name='eb_balance_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_balance_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_balance_by_pk = sgqlc.types.Field('eb_balance', graphql_name='eb_balance_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_bank_account = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_bank_account'))), graphql_name='eb_bank_account', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_bank_account_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_bank_account_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_bank_account_aggregate'), graphql_name='eb_bank_account_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_bank_account_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_bank_account_by_pk = sgqlc.types.Field('eb_bank_account', graphql_name='eb_bank_account_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_keys'))), graphql_name='eb_keys', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_keys_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_keys_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_keys_aggregate'), graphql_name='eb_keys_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_keys_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_keys_by_pk = sgqlc.types.Field('eb_keys', graphql_name='eb_keys_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_session_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_session_info'))), graphql_name='eb_session_info', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_session_info_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_session_info_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_session_info_aggregate'), graphql_name='eb_session_info_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_session_info_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_session_info_by_pk = sgqlc.types.Field('eb_session_info', graphql_name='eb_session_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_transaction = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_transaction'))), graphql_name='eb_transaction', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_transaction_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_transaction_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_transaction_aggregate'), graphql_name='eb_transaction_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_transaction_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_transaction_by_pk = sgqlc.types.Field('eb_transaction', graphql_name='eb_transaction_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    forecast = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast'))), graphql_name='forecast', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_aggregate = sgqlc.types.Field(sgqlc.types.non_null('forecast_aggregate'), graphql_name='forecast_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_by_pk = sgqlc.types.Field('forecast', graphql_name='forecast_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    forecast_event = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast_event'))), graphql_name='forecast_event', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_event_aggregate = sgqlc.types.Field(sgqlc.types.non_null('forecast_event_aggregate'), graphql_name='forecast_event_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_event_by_pk = sgqlc.types.Field('forecast_event', graphql_name='forecast_event_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group'))), graphql_name='group', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_bool_exp, graphql_name='where', default=None)),
))
    )
    group_aggregate = sgqlc.types.Field(sgqlc.types.non_null('group_aggregate'), graphql_name='group_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_bool_exp, graphql_name='where', default=None)),
))
    )
    group_by_pk = sgqlc.types.Field('group', graphql_name='group_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    group_relation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group_relation'))), graphql_name='group_relation', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relation_aggregate = sgqlc.types.Field(sgqlc.types.non_null('group_relation_aggregate'), graphql_name='group_relation_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relation_by_pk = sgqlc.types.Field('group_relation', graphql_name='group_relation_by_pk', args=sgqlc.types.ArgDict((
        ('primary_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='primary_id', default=None)),
        ('secondary_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='secondary_id', default=None)),
))
    )
    invoice = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice'))), graphql_name='invoice', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_aggregate = sgqlc.types.Field(sgqlc.types.non_null('invoice_aggregate'), graphql_name='invoice_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_by_pk = sgqlc.types.Field('invoice', graphql_name='invoice_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    invoice_type_enum = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice_type_enum'))), graphql_name='invoice_type_enum', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_type_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_type_enum_aggregate = sgqlc.types.Field(sgqlc.types.non_null('invoice_type_enum_aggregate'), graphql_name='invoice_type_enum_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_type_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_type_enum_by_pk = sgqlc.types.Field('invoice_type_enum', graphql_name='invoice_type_enum_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    netvisor_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('netvisor_info'))), graphql_name='netvisor_info', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(netvisor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    netvisor_info_aggregate = sgqlc.types.Field(sgqlc.types.non_null('netvisor_info_aggregate'), graphql_name='netvisor_info_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(netvisor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    netvisor_info_by_pk = sgqlc.types.Field('netvisor_info', graphql_name='netvisor_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    payment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('payment'))), graphql_name='payment', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(payment_bool_exp, graphql_name='where', default=None)),
))
    )
    payment_aggregate = sgqlc.types.Field(sgqlc.types.non_null('payment_aggregate'), graphql_name='payment_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(payment_bool_exp, graphql_name='where', default=None)),
))
    )
    payment_by_pk = sgqlc.types.Field('payment', graphql_name='payment_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    procountor_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('procountor_info'))), graphql_name='procountor_info', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(procountor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    procountor_info_aggregate = sgqlc.types.Field(sgqlc.types.non_null('procountor_info_aggregate'), graphql_name='procountor_info_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(procountor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    procountor_info_by_pk = sgqlc.types.Field('procountor_info', graphql_name='procountor_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('role'))), graphql_name='role', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(role_bool_exp, graphql_name='where', default=None)),
))
    )
    role_aggregate = sgqlc.types.Field(sgqlc.types.non_null('role_aggregate'), graphql_name='role_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(role_bool_exp, graphql_name='where', default=None)),
))
    )
    role_by_pk = sgqlc.types.Field('role', graphql_name='role_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    roles_customers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('roles_customers'))), graphql_name='roles_customers', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    roles_customers_aggregate = sgqlc.types.Field(sgqlc.types.non_null('roles_customers_aggregate'), graphql_name='roles_customers_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    source_enum = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('source_enum'))), graphql_name='source_enum', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(source_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    source_enum_aggregate = sgqlc.types.Field(sgqlc.types.non_null('source_enum_aggregate'), graphql_name='source_enum_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(source_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    source_enum_by_pk = sgqlc.types.Field('source_enum', graphql_name='source_enum_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )


class role(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'roles_customers', 'roles_customers_aggregate', 'time_created', 'time_updated')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    roles_customers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('roles_customers'))), graphql_name='roles_customers', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    roles_customers_aggregate = sgqlc.types.Field(sgqlc.types.non_null('roles_customers_aggregate'), graphql_name='roles_customers_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class role_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('role_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(role))), graphql_name='nodes')


class role_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('role_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('role_max_fields', graphql_name='max')
    min = sgqlc.types.Field('role_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('role_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('role_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('role_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('role_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('role_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('role_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('role_variance_fields', graphql_name='variance')


class role_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class role_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'time_created', 'time_updated')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class role_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('description', 'id', 'name', 'time_created', 'time_updated')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    time_created = sgqlc.types.Field(timestamptz, graphql_name='time_created')
    time_updated = sgqlc.types.Field(timestamptz, graphql_name='time_updated')


class role_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(role))), graphql_name='returning')


class role_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class role_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class role_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class role_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Int, graphql_name='id')


class role_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class role_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class role_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Float, graphql_name='id')


class roles_customers(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('customer', 'role', 'role_id', 'user_id')
    customer = sgqlc.types.Field('customer', graphql_name='customer')
    role = sgqlc.types.Field('role', graphql_name='role')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')


class roles_customers_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('roles_customers_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers))), graphql_name='nodes')


class roles_customers_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('roles_customers_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('roles_customers_max_fields', graphql_name='max')
    min = sgqlc.types.Field('roles_customers_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('roles_customers_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('roles_customers_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('roles_customers_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('roles_customers_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('roles_customers_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('roles_customers_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('roles_customers_variance_fields', graphql_name='variance')


class roles_customers_avg_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Float, graphql_name='role_id')
    user_id = sgqlc.types.Field(Float, graphql_name='user_id')


class roles_customers_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')


class roles_customers_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')


class roles_customers_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers))), graphql_name='returning')


class roles_customers_stddev_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Float, graphql_name='role_id')
    user_id = sgqlc.types.Field(Float, graphql_name='user_id')


class roles_customers_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Float, graphql_name='role_id')
    user_id = sgqlc.types.Field(Float, graphql_name='user_id')


class roles_customers_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Float, graphql_name='role_id')
    user_id = sgqlc.types.Field(Float, graphql_name='user_id')


class roles_customers_sum_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Int, graphql_name='role_id')
    user_id = sgqlc.types.Field(Int, graphql_name='user_id')


class roles_customers_var_pop_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Float, graphql_name='role_id')
    user_id = sgqlc.types.Field(Float, graphql_name='user_id')


class roles_customers_var_samp_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Float, graphql_name='role_id')
    user_id = sgqlc.types.Field(Float, graphql_name='user_id')


class roles_customers_variance_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(Float, graphql_name='role_id')
    user_id = sgqlc.types.Field(Float, graphql_name='user_id')


class source_enum(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id', 'invoices', 'invoices_aggregate')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    invoices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(invoice))), graphql_name='invoices', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoices_aggregate = sgqlc.types.Field(sgqlc.types.non_null(invoice_aggregate), graphql_name='invoices_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )


class source_enum_aggregate(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('source_enum_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(source_enum))), graphql_name='nodes')


class source_enum_aggregate_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('count', 'max', 'min')
    count = sgqlc.types.Field(Int, graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('source_enum_max_fields', graphql_name='max')
    min = sgqlc.types.Field('source_enum_min_fields', graphql_name='min')


class source_enum_max_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(String, graphql_name='id')


class source_enum_min_fields(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('id',)
    id = sgqlc.types.Field(String, graphql_name='id')


class source_enum_mutation_response(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(source_enum))), graphql_name='returning')


class subscription_root(sgqlc.types.Type):
    __schema__ = schema_dev
    __field_names__ = ('company', 'company_aggregate', 'company_by_pk', 'customer', 'customer_aggregate', 'customer_by_pk', 'eb_balance', 'eb_balance_aggregate', 'eb_balance_by_pk', 'eb_bank_account', 'eb_bank_account_aggregate', 'eb_bank_account_by_pk', 'eb_keys', 'eb_keys_aggregate', 'eb_keys_by_pk', 'eb_session_info', 'eb_session_info_aggregate', 'eb_session_info_by_pk', 'eb_transaction', 'eb_transaction_aggregate', 'eb_transaction_by_pk', 'forecast', 'forecast_aggregate', 'forecast_by_pk', 'forecast_event', 'forecast_event_aggregate', 'forecast_event_by_pk', 'group', 'group_aggregate', 'group_by_pk', 'group_relation', 'group_relation_aggregate', 'group_relation_by_pk', 'invoice', 'invoice_aggregate', 'invoice_by_pk', 'invoice_type_enum', 'invoice_type_enum_aggregate', 'invoice_type_enum_by_pk', 'netvisor_info', 'netvisor_info_aggregate', 'netvisor_info_by_pk', 'payment', 'payment_aggregate', 'payment_by_pk', 'procountor_info', 'procountor_info_aggregate', 'procountor_info_by_pk', 'role', 'role_aggregate', 'role_by_pk', 'roles_customers', 'roles_customers_aggregate', 'source_enum', 'source_enum_aggregate', 'source_enum_by_pk')
    company = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('company'))), graphql_name='company', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(company_bool_exp, graphql_name='where', default=None)),
))
    )
    company_aggregate = sgqlc.types.Field(sgqlc.types.non_null('company_aggregate'), graphql_name='company_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(company_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(company_bool_exp, graphql_name='where', default=None)),
))
    )
    company_by_pk = sgqlc.types.Field('company', graphql_name='company_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    customer = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('customer'))), graphql_name='customer', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(customer_bool_exp, graphql_name='where', default=None)),
))
    )
    customer_aggregate = sgqlc.types.Field(sgqlc.types.non_null('customer_aggregate'), graphql_name='customer_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(customer_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(customer_bool_exp, graphql_name='where', default=None)),
))
    )
    customer_by_pk = sgqlc.types.Field('customer', graphql_name='customer_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_balance = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_balance'))), graphql_name='eb_balance', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_balance_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_balance_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_balance_aggregate'), graphql_name='eb_balance_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_balance_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_balance_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_balance_by_pk = sgqlc.types.Field('eb_balance', graphql_name='eb_balance_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_bank_account = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_bank_account'))), graphql_name='eb_bank_account', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_bank_account_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_bank_account_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_bank_account_aggregate'), graphql_name='eb_bank_account_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_bank_account_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_bank_account_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_bank_account_by_pk = sgqlc.types.Field('eb_bank_account', graphql_name='eb_bank_account_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_keys'))), graphql_name='eb_keys', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_keys_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_keys_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_keys_aggregate'), graphql_name='eb_keys_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_keys_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_keys_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_keys_by_pk = sgqlc.types.Field('eb_keys', graphql_name='eb_keys_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_session_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_session_info'))), graphql_name='eb_session_info', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_session_info_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_session_info_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_session_info_aggregate'), graphql_name='eb_session_info_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_session_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_session_info_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_session_info_by_pk = sgqlc.types.Field('eb_session_info', graphql_name='eb_session_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eb_transaction = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('eb_transaction'))), graphql_name='eb_transaction', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_transaction_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_transaction_aggregate = sgqlc.types.Field(sgqlc.types.non_null('eb_transaction_aggregate'), graphql_name='eb_transaction_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(eb_transaction_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(eb_transaction_bool_exp, graphql_name='where', default=None)),
))
    )
    eb_transaction_by_pk = sgqlc.types.Field('eb_transaction', graphql_name='eb_transaction_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    forecast = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast'))), graphql_name='forecast', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_aggregate = sgqlc.types.Field(sgqlc.types.non_null('forecast_aggregate'), graphql_name='forecast_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_by_pk = sgqlc.types.Field('forecast', graphql_name='forecast_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    forecast_event = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('forecast_event'))), graphql_name='forecast_event', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_event_aggregate = sgqlc.types.Field(sgqlc.types.non_null('forecast_event_aggregate'), graphql_name='forecast_event_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(forecast_event_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(forecast_event_bool_exp, graphql_name='where', default=None)),
))
    )
    forecast_event_by_pk = sgqlc.types.Field('forecast_event', graphql_name='forecast_event_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group'))), graphql_name='group', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_bool_exp, graphql_name='where', default=None)),
))
    )
    group_aggregate = sgqlc.types.Field(sgqlc.types.non_null('group_aggregate'), graphql_name='group_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_bool_exp, graphql_name='where', default=None)),
))
    )
    group_by_pk = sgqlc.types.Field('group', graphql_name='group_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    group_relation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('group_relation'))), graphql_name='group_relation', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relation_aggregate = sgqlc.types.Field(sgqlc.types.non_null('group_relation_aggregate'), graphql_name='group_relation_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(group_relation_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(group_relation_bool_exp, graphql_name='where', default=None)),
))
    )
    group_relation_by_pk = sgqlc.types.Field('group_relation', graphql_name='group_relation_by_pk', args=sgqlc.types.ArgDict((
        ('primary_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='primary_id', default=None)),
        ('secondary_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='secondary_id', default=None)),
))
    )
    invoice = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice'))), graphql_name='invoice', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_aggregate = sgqlc.types.Field(sgqlc.types.non_null('invoice_aggregate'), graphql_name='invoice_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_by_pk = sgqlc.types.Field('invoice', graphql_name='invoice_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    invoice_type_enum = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('invoice_type_enum'))), graphql_name='invoice_type_enum', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_type_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_type_enum_aggregate = sgqlc.types.Field(sgqlc.types.non_null('invoice_type_enum_aggregate'), graphql_name='invoice_type_enum_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(invoice_type_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(invoice_type_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    invoice_type_enum_by_pk = sgqlc.types.Field('invoice_type_enum', graphql_name='invoice_type_enum_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    netvisor_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('netvisor_info'))), graphql_name='netvisor_info', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(netvisor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    netvisor_info_aggregate = sgqlc.types.Field(sgqlc.types.non_null('netvisor_info_aggregate'), graphql_name='netvisor_info_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(netvisor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(netvisor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    netvisor_info_by_pk = sgqlc.types.Field('netvisor_info', graphql_name='netvisor_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    payment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('payment'))), graphql_name='payment', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(payment_bool_exp, graphql_name='where', default=None)),
))
    )
    payment_aggregate = sgqlc.types.Field(sgqlc.types.non_null('payment_aggregate'), graphql_name='payment_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(payment_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(payment_bool_exp, graphql_name='where', default=None)),
))
    )
    payment_by_pk = sgqlc.types.Field('payment', graphql_name='payment_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    procountor_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('procountor_info'))), graphql_name='procountor_info', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(procountor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    procountor_info_aggregate = sgqlc.types.Field(sgqlc.types.non_null('procountor_info_aggregate'), graphql_name='procountor_info_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(procountor_info_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(procountor_info_bool_exp, graphql_name='where', default=None)),
))
    )
    procountor_info_by_pk = sgqlc.types.Field('procountor_info', graphql_name='procountor_info_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('role'))), graphql_name='role', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(role_bool_exp, graphql_name='where', default=None)),
))
    )
    role_aggregate = sgqlc.types.Field(sgqlc.types.non_null('role_aggregate'), graphql_name='role_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(role_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(role_bool_exp, graphql_name='where', default=None)),
))
    )
    role_by_pk = sgqlc.types.Field('role', graphql_name='role_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    roles_customers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('roles_customers'))), graphql_name='roles_customers', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    roles_customers_aggregate = sgqlc.types.Field(sgqlc.types.non_null('roles_customers_aggregate'), graphql_name='roles_customers_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(roles_customers_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(roles_customers_bool_exp, graphql_name='where', default=None)),
))
    )
    source_enum = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('source_enum'))), graphql_name='source_enum', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(source_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    source_enum_aggregate = sgqlc.types.Field(sgqlc.types.non_null('source_enum_aggregate'), graphql_name='source_enum_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(source_enum_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(source_enum_bool_exp, graphql_name='where', default=None)),
))
    )
    source_enum_by_pk = sgqlc.types.Field('source_enum', graphql_name='source_enum_by_pk', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema_dev.query_type = query_root
schema_dev.mutation_type = mutation_root
schema_dev.subscription_type = subscription_root

