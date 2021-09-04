from rest_framework import serializers

from .models import Employee, Organization


class ModelSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        repr_dict = super(ModelSerializer, self).to_representation(value)
        return dict((k, v) for k, v in repr_dict.items()
                    if v not in [None, [], '', {}])


class OrganizationSerializer(ModelSerializer):
    employees = serializers.SlugRelatedField(
        slug_field='get_full_name',
        queryset=Employee.objects.all(),
        many=True
    )

    class Meta:
        fields = ('id', 'name', 'address', 'description', 'employees')
        model = Organization


class EmployeeSerializer(ModelSerializer):
    organization = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Organization.objects.all())
    fullname = serializers.ReadOnlyField(source='get_full_name')

    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'middlename',
                  'fullname', 'organization',)
