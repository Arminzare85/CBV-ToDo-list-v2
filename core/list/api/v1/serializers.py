from rest_framework import serializers
from list.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    # snippet = serializers.CharField(max_length=255, read_only=True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            # 'snippet',
            'description',
            'priority',
            'is_completed',
            'created_at',
            'absolute_url',
        ]
    def get_absolute_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(
                f'/todo/api/v1/task/{obj.id}/'
            )