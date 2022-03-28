from rest_framework import generics
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from project.app.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "name",
        ]


class ContractPaginatedResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    results = ContractSerializer(many=True)


class ContractPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class ContractListAPIView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    pagination_class = ContractPagination

    def get(self, request, *args, **kwargs):
        contracts = self.get_queryset()
        page = self.paginate_queryset_if_page_param(
            contracts
        )
        return Response(  # this is rest_framework.response's Response model
            ContractPaginatedResponseSerializer(
                {"count": contracts.count(), "results": page}
            ).data
        )

    def paginate_queryset_if_page_param(self, queryset):
        if self.pagination_class.page_query_param in self.request.query_params.keys():
            return self.paginate_queryset(queryset)
