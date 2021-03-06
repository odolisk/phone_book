from rest_framework import filters, serializers

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
                  'email')
        model = User


class ModelSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        repr_dict = super(ModelSerializer, self).to_representation(value)
        return dict((k, v) for k, v in repr_dict.items()
                    if v not in [None, [], '', {}])


class EmployeeWriteSerializer(ModelSerializer):
    organization = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = Employee
        fields = ('pk', 'name', 'middlename', 'surname', 'personal_phone',
                  'work_phone', 'fax', 'organization')
        read_only_fields = ('organization', )

        def validate(self, data):
            if not (data['work_phone']
                    or data['personal_phone']
                    or data['fax']):
                raise serializers.ValidationError(
                    'Должен быть заполнен хотя бы один телефон')
            name = data['name']
            middlename = data['middlename']
            surname = data['surname']
            organization = data['organization']
            if Employee.objects.get(
                name=name, middlename=middlename,
                    surname=surname, organization=organization):
                raise serializers.ValidationError(
                    f'Сотрудник {surname} {name} {middlename}'
                    f'уже есть в организации {organization}!')
            return data


class EmployeeReadSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeListSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'position',
                  'work_phone', 'personal_phone')


class OrganizationListSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('name', 'employee__full_name')

    class Meta:
        fields = ('id', 'name', 'address', 'description', 'author')
        model = Organization


class OrganizationRetriveSerializer(ModelSerializer):
    employees = EmployeeListSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name', 'address', 'description', 'employees')
        model = Organization


class EditorAddSerializer(serializers.Serializer):
    pass
