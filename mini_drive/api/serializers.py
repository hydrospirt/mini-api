import re
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from files.models import TextFile


class TextFileSerializer(serializers.ModelSerializer):
    """Сериализатор для текстового файла"""
    name = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(queryset=TextFile.objects.all())]
    )
    pub_date = serializers.DateTimeField(
        read_only=True
    )

    class Meta:
        fields = ('name', 'data', 'pub_date')
        model = TextFile

    def validate_name(self, value):
        pattern = r'^[A-Za-zА-Яа-я0-9_]+\.txt$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                r'Поле "username" дожно содержать символы: ^[A-Za-zА-Яа-я0-9_]+\.txt$'
            )
        return value
