#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import demo_pb2 as demo__pb2


class CartServiceStub(object):
  """-----------------Cart service-----------------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddItem = channel.unary_unary(
        '/hipstershop.CartService/AddItem',
        request_serializer=demo__pb2.AddItemRequest.SerializeToString,
        response_deserializer=demo__pb2.Empty.FromString,
        )
    self.GetCart = channel.unary_unary(
        '/hipstershop.CartService/GetCart',
        request_serializer=demo__pb2.GetCartRequest.SerializeToString,
        response_deserializer=demo__pb2.Cart.FromString,
        )
    self.EmptyCart = channel.unary_unary(
        '/hipstershop.CartService/EmptyCart',
        request_serializer=demo__pb2.EmptyCartRequest.SerializeToString,
        response_deserializer=demo__pb2.Empty.FromString,
        )


class CartServiceServicer(object):
  """-----------------Cart service-----------------

  """

  def AddItem(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EmptyCart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CartServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddItem': grpc.unary_unary_rpc_method_handler(
          servicer.AddItem,
          request_deserializer=demo__pb2.AddItemRequest.FromString,
          response_serializer=demo__pb2.Empty.SerializeToString,
      ),
      'GetCart': grpc.unary_unary_rpc_method_handler(
          servicer.GetCart,
          request_deserializer=demo__pb2.GetCartRequest.FromString,
          response_serializer=demo__pb2.Cart.SerializeToString,
      ),
      'EmptyCart': grpc.unary_unary_rpc_method_handler(
          servicer.EmptyCart,
          request_deserializer=demo__pb2.EmptyCartRequest.FromString,
          response_serializer=demo__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.CartService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class RecommendationServiceStub(object):
  """---------------Recommendation service----------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListRecommendations = channel.unary_unary(
        '/hipstershop.RecommendationService/ListRecommendations',
        request_serializer=demo__pb2.ListRecommendationsRequest.SerializeToString,
        response_deserializer=demo__pb2.ListRecommendationsResponse.FromString,
        )


class RecommendationServiceServicer(object):
  """---------------Recommendation service----------

  """

  def ListRecommendations(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RecommendationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListRecommendations': grpc.unary_unary_rpc_method_handler(
          servicer.ListRecommendations,
          request_deserializer=demo__pb2.ListRecommendationsRequest.FromString,
          response_serializer=demo__pb2.ListRecommendationsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.RecommendationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ProductCatalogServiceStub(object):
  """---------------Product Catalog----------------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListProducts = channel.unary_unary(
        '/hipstershop.ProductCatalogService/ListProducts',
        request_serializer=demo__pb2.Empty.SerializeToString,
        response_deserializer=demo__pb2.ListProductsResponse.FromString,
        )
    self.GetProduct = channel.unary_unary(
        '/hipstershop.ProductCatalogService/GetProduct',
        request_serializer=demo__pb2.GetProductRequest.SerializeToString,
        response_deserializer=demo__pb2.Product.FromString,
        )
    self.SearchProducts = channel.unary_unary(
        '/hipstershop.ProductCatalogService/SearchProducts',
        request_serializer=demo__pb2.SearchProductsRequest.SerializeToString,
        response_deserializer=demo__pb2.SearchProductsResponse.FromString,
        )


class ProductCatalogServiceServicer(object):
  """---------------Product Catalog----------------

  """

  def ListProducts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProduct(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchProducts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProductCatalogServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListProducts': grpc.unary_unary_rpc_method_handler(
          servicer.ListProducts,
          request_deserializer=demo__pb2.Empty.FromString,
          response_serializer=demo__pb2.ListProductsResponse.SerializeToString,
      ),
      'GetProduct': grpc.unary_unary_rpc_method_handler(
          servicer.GetProduct,
          request_deserializer=demo__pb2.GetProductRequest.FromString,
          response_serializer=demo__pb2.Product.SerializeToString,
      ),
      'SearchProducts': grpc.unary_unary_rpc_method_handler(
          servicer.SearchProducts,
          request_deserializer=demo__pb2.SearchProductsRequest.FromString,
          response_serializer=demo__pb2.SearchProductsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.ProductCatalogService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ShippingServiceStub(object):
  """---------------Shipping Service----------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetQuote = channel.unary_unary(
        '/hipstershop.ShippingService/GetQuote',
        request_serializer=demo__pb2.GetQuoteRequest.SerializeToString,
        response_deserializer=demo__pb2.GetQuoteResponse.FromString,
        )
    self.ShipOrder = channel.unary_unary(
        '/hipstershop.ShippingService/ShipOrder',
        request_serializer=demo__pb2.ShipOrderRequest.SerializeToString,
        response_deserializer=demo__pb2.ShipOrderResponse.FromString,
        )


class ShippingServiceServicer(object):
  """---------------Shipping Service----------

  """

  def GetQuote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShipOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ShippingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetQuote': grpc.unary_unary_rpc_method_handler(
          servicer.GetQuote,
          request_deserializer=demo__pb2.GetQuoteRequest.FromString,
          response_serializer=demo__pb2.GetQuoteResponse.SerializeToString,
      ),
      'ShipOrder': grpc.unary_unary_rpc_method_handler(
          servicer.ShipOrder,
          request_deserializer=demo__pb2.ShipOrderRequest.FromString,
          response_serializer=demo__pb2.ShipOrderResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.ShippingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CurrencyServiceStub(object):
  """-----------------Currency service-----------------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSupportedCurrencies = channel.unary_unary(
        '/hipstershop.CurrencyService/GetSupportedCurrencies',
        request_serializer=demo__pb2.Empty.SerializeToString,
        response_deserializer=demo__pb2.GetSupportedCurrenciesResponse.FromString,
        )
    self.Convert = channel.unary_unary(
        '/hipstershop.CurrencyService/Convert',
        request_serializer=demo__pb2.CurrencyConversionRequest.SerializeToString,
        response_deserializer=demo__pb2.Money.FromString,
        )


class CurrencyServiceServicer(object):
  """-----------------Currency service-----------------

  """

  def GetSupportedCurrencies(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Convert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CurrencyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSupportedCurrencies': grpc.unary_unary_rpc_method_handler(
          servicer.GetSupportedCurrencies,
          request_deserializer=demo__pb2.Empty.FromString,
          response_serializer=demo__pb2.GetSupportedCurrenciesResponse.SerializeToString,
      ),
      'Convert': grpc.unary_unary_rpc_method_handler(
          servicer.Convert,
          request_deserializer=demo__pb2.CurrencyConversionRequest.FromString,
          response_serializer=demo__pb2.Money.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.CurrencyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PaymentServiceStub(object):
  """-------------Payment service-----------------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Charge = channel.unary_unary(
        '/hipstershop.PaymentService/Charge',
        request_serializer=demo__pb2.ChargeRequest.SerializeToString,
        response_deserializer=demo__pb2.ChargeResponse.FromString,
        )


class PaymentServiceServicer(object):
  """-------------Payment service-----------------

  """

  def Charge(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PaymentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Charge': grpc.unary_unary_rpc_method_handler(
          servicer.Charge,
          request_deserializer=demo__pb2.ChargeRequest.FromString,
          response_serializer=demo__pb2.ChargeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.PaymentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class EmailServiceStub(object):
  """-------------Email service-----------------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendOrderConfirmation = channel.unary_unary(
        '/hipstershop.EmailService/SendOrderConfirmation',
        request_serializer=demo__pb2.SendOrderConfirmationRequest.SerializeToString,
        response_deserializer=demo__pb2.Empty.FromString,
        )


class EmailServiceServicer(object):
  """-------------Email service-----------------

  """

  def SendOrderConfirmation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EmailServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendOrderConfirmation': grpc.unary_unary_rpc_method_handler(
          servicer.SendOrderConfirmation,
          request_deserializer=demo__pb2.SendOrderConfirmationRequest.FromString,
          response_serializer=demo__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.EmailService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CheckoutServiceStub(object):
  """-------------Checkout service-----------------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateOrder = channel.unary_unary(
        '/hipstershop.CheckoutService/CreateOrder',
        request_serializer=demo__pb2.CreateOrderRequest.SerializeToString,
        response_deserializer=demo__pb2.CreateOrderResponse.FromString,
        )
    self.PlaceOrder = channel.unary_unary(
        '/hipstershop.CheckoutService/PlaceOrder',
        request_serializer=demo__pb2.PlaceOrderRequest.SerializeToString,
        response_deserializer=demo__pb2.PlaceOrderResponse.FromString,
        )


class CheckoutServiceServicer(object):
  """-------------Checkout service-----------------

  """

  def CreateOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PlaceOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CheckoutServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CreateOrder,
          request_deserializer=demo__pb2.CreateOrderRequest.FromString,
          response_serializer=demo__pb2.CreateOrderResponse.SerializeToString,
      ),
      'PlaceOrder': grpc.unary_unary_rpc_method_handler(
          servicer.PlaceOrder,
          request_deserializer=demo__pb2.PlaceOrderRequest.FromString,
          response_serializer=demo__pb2.PlaceOrderResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hipstershop.CheckoutService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
