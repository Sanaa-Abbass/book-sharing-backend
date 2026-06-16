from rest_framework import serializers
from .models import User, InvitationCode


class RegisterSerializer(serializers.ModelSerializer):

    invitation_code = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'invitation_code'
        ]

    def create(self, validated_data):

        code = validated_data.pop('invitation_code')

        try:
            invitation = InvitationCode.objects.get(
                code=code,
                is_active=True
            )
        except InvitationCode.DoesNotExist:
            raise serializers.ValidationError(
                {
                    'invitation_code':
                    'Invalid invitation code.'
                }
            )

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            invitation_code=invitation
        )

        return user