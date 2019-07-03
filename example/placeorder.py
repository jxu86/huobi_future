from huobi import RequestClient
from huobi.model import *
import time




pair = 'eoseth'
# request_client = RequestClient(api_key="94d4dbd5-yh4fhmvs5k-746262cd-a7869",
#                                secret_key="66d97ea2-93176177-2c372af8-2d4cb")

# request_client = RequestClient(api_key="48b7e0cc-4ed9b857-32995061-vqgdf4gsga",
#                                secret_key="c1f3cbe5-1ba64f39-c42322c5-88455")


request_client_future = RequestClient(secret_key="010e5e9b-3e0f0fd4-e013b1ff-65b0c",
                               api_key="05a49add-d430ac2c-ed2htwf5tf-37363",
                               url='https://api.hbdm.com')

print('request_client_future=>', request_client_future)

account_info = request_client_future.get_account_balance()
for balance in account_info.balances:
    print('account==>', balance)
    print('===>', balance.currency)
    print('===>', balance.balance)
    print('===>', balance.position)
    print('===>', balance.frozen)
    print('===>', balance.available)

# exchange_info = request_client.get_exchange_info()
# print('exchange_info==>', exchange_info.symbol_list)
# print('exchange_info==>', exchange_info.currencies)
# print(exchange_info.symbol_list[-1].symbol)
# print(exchange_info.symbol_list[-1].base_currency)
# print(exchange_info.symbol_list[-1].quote_currency)
# order_id = request_client.create_order(pair, AccountType.SPOT, OrderType.BUY_LIMIT, 0.1, 0.0011111)
# print('order_id=>', order_id)
# order_info = request_client.get_order(pair, '38124135748')
# print('order_info=>', order_info)
# # time.sleep(20)
# o = order_info
# print('==>', o.order_id)
# print('==>', o.amount)
# print('==>', o.price)

# print('==>', o.symbol)
# print('==>', o.order_type)
# print('==>', o.filled_amount)
# print('==>', o.state)
# print('==>', o.created_timestamp)
# print('==>', o.source)

# request_client.cancel_order(pair, order_id)



# open_orders = request_client.get_open_orders(pair, AccountType.SPOT)
# print('open_orders==>', open_orders) 
# for o in open_orders:
#     print('==>', o.order_id)
#     print('==>', o.amount)
#     print('==>', o.price)
    
#     print('==>', o.symbol)
#     print('==>', o.order_type)
#     print('==>', o.filled_amount)
#     print('==>', o.state)
#     print('==>', o.created_timestamp)
#     print('==>', o.source)



# balances = request_client.get_account_balance()
# print('balances=>', balances)
# print('balances type=>', type(balances))
# for b in balances:
#     print('type=>', type(b))
#     print('===>', b.id)
#     print('===>', b.account_type)
#     print('===>', b.account_state)
#     # print('===>', b.balances)

#     for bl in b.get_balance('eth'):
#         print('bl=>', bl, '    ', bl.balance)


# spot_balance = request_client.get_account_balance_by_account_type('spot')
# print('spot_balance=>', spot_balance)
# b = spot_balance
# print('type=>', type(b))
# print('===>', b.id)
# print('===>', b.account_type)
# print('===>', b.account_state)

# for balance in b.balances:
#     print('balance===>', balance)
#     print('balance===>', balance.currency)
#     print('balance===>', balance.balance_type)
#     print('balance===>', balance.currency)
# print('===>', spot_balance.get_balance('eth'))
# for bl in spot_balance.get_balance('eth'):
#     if bl.balance_type == BalanceType.TRADE:
#         print('===>',bl.currency)
#         print('===>',bl.balance_type)
#         print('===>',type(bl.balance))

# balance = 0
# for b in spot_balance.get_balance('eth'):
#     if b.balance_type == BalanceType.TRADE or b.balance_type == BalanceType.FROZEN:
#         balance += b.balance

# print('balance=>', balance)
# _api = request_client
# def get_coin_info(instrument_id):
#     exchange_info = _api.get_exchange_info()
#     symbol_list = exchange_info.symbol_list

#     for sl in symbol_list:
#         if sl.symbol == instrument_id:
#             return {
#                 'instrument_id': instrument_id,
#                 'base_currency': sl.base_currency,
#                 'quote_currency': sl.quote_currency,
#                 'tick_size': sl.price_precision,
#                 'size_increment': sl.amount_precision
#             }


# info = get_coin_info('eoseth')
# print('info=>', info)
# orders_states = 
# orders = request_client.get_historical_orders('eosusdt','filled',start_date='2019-06-25', end_date='2019-06-25', size=1000)
# print('orders ==>', orders)
# for o in orders:
#     print('=================>', o.order_id)
#     # print('==>', o.amount)
#     # print('==>', o.price)
#     # print('==>', o.symbol)
#     # print('==>', o.order_type)
#     # print('==>', o.filled_amount)
#     # print('==>', o.state)
#     print('==>', o.created_timestamp)
    # print('==>', o.source)
# ret = request_client.get_last_trade('eoseth')
# print('ret =>', ret.price)

# AccountType
# def get_account_info():
#         account_balances = request_client.get_account_balance_by_account_type(
#             AccountType.MARGIN)
#         details_obj = {}
#         details = []
#         for b in account_balances.balances:
#             if b.balance:
#                 if b.currency not in details_obj:
#                     if b.balance_type == BalanceType.TRADE:
#                         details_obj[b.currency] = {'currency': b.currency.upper(), 'frozen': 0, 'balance': b.balance, 'available': b.balance}
#                     elif b.balance_type == BalanceType.FROZEN:
#                         details_obj[b.currency] = {'currency': b.currency.upper(), 'frozen': b.balance, 'balance': b.balance, 'available': 0}

#                 else:
#                     if b.balance_type == BalanceType.TRADE:
#                         details_obj[b.currency]['available'] += b.balance
#                         details_obj[b.currency]['balance'] += b.balance

#                     elif b.balance_type == BalanceType.FROZEN:
#                         details_obj[b.currency]['frozen'] += b.balance
#                         details_obj[b.currency]['balance'] += b.balance
                
#         return list(details_obj.values())


# print('=======>', get_account_info())