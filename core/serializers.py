from rest_framework import serializers

from .models import Project, Skill, SkillCategory, Certification


class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = serializers.SerializerMethodField()
    highlights = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "title", "year", "summary", "tech_stack", "highlights", "link"]

    def get_tech_stack(self, obj):
        return obj.tech_list()

    def get_highlights(self, obj):
        return obj.bullets()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = SkillCategory
        fields = ["id", "name", "skills"]


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ["id", "name", "provider", "year"]
