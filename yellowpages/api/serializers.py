from rest_framework import serializers

from .models import Employee, Organization, User


def phone_required(fields):
    if all(value is None for value in fields):
        raise serializers.ValidationError('This field is required')


class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserObtainTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=150)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('first_name', 'last_name', 'username',
                  'bio', 'email', 'role')
        model = User


class ModelSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        repr_dict = super(ModelSerializer, self).to_representation(value)
        return dict((k, v) for k, v in repr_dict.items()
                    if v not in [None, [], '', {}])


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeListSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'position',
                  'work_phone', 'personal_phone')
        validators = [
            phone_required(
                fields=('work_phone', 'personal_phone')
            )
        ]


class OrganizationsListSerializer(ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'address', 'description')
        model = Organization


class OrganizationsRetriveSerializer(ModelSerializer):
    employees = EmployeeListSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name', 'address', 'description', 'employees')
        model = Organization
