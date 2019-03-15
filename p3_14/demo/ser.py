from rest_framework import serializers
from .models import *
class StuSer(serializers.Serializer):
    stu_name = serializers.CharField()
    code = serializers.CharField()
    cls_id = serializers.CharField(write_only=True)
    cls = serializers.HyperlinkedRelatedField(lookup_field='id',lookup_url_kwarg='pk',view_name='class',read_only=True)
    def create(self, validated_data):
        a = Stuendt.objects.create(**validated_data)
        return a
class ClsSer(serializers.ModelSerializer):
    class Meta:
        model = Cls
        fields = '__all__'