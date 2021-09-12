# from django.db import DataError

# from rest_framework.exceptions import ValidationError
# from rest_framework.validators import UniqueValidator


# def qs_exists(queryset):
#     try:
#         return queryset.exists()
#     except (TypeError, ValueError, DataError):
#         return False


# class UniquePhoneValidator(UniqueValidator):

#     message = 'Это поле должно быть уникальным.'

#     def __call__(self, value, serializer_field):
#         field_name = serializer_field.source_attrs[-1]
#         instance = getattr(serializer_field.parent, 'instance', None)

#         queryset = self.queryset
#         queryset = self.filter_queryset(value, queryset, field_name)
#         queryset = self.exclude_current_instance(queryset, instance)
#         if qs_exists(queryset) and queryset != '':
#             raise ValidationError(self.message, code='unique')
