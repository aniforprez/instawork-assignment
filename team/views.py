from django.views import View
from django.http import JsonResponse
import json
from .models import TeamMember
from .serializers import TeamMemberSerializer
from django.forms.models import model_to_dict


class MemberListView(View):
    def get(self, request):
        team_members = TeamMember.objects.all()
        team_data = TeamMemberSerializer(team_members, many=True)
        return JsonResponse({"data": team_data.data}, safe=False)

    def post(self, request):
        input_json = json.loads(request.body)
        serializer = TeamMemberSerializer(data=input_json)
        if not serializer.is_valid():
            return JsonResponse({"errors": serializer.errors})

        new_member = serializer.save()
        return JsonResponse(model_to_dict(new_member), status=201)

class MemberView(View):
    def get(self, request, **kwargs):
        member_id = kwargs.get("member_id")
        if not member_id:
            return JsonResponse({}, status=404)

        try:
            member = TeamMember.objects.get(member_id=member_id)
        except TeamMember.DoesNotExist:
            return JsonResponse({}, status=404)

        return JsonResponse(TeamMemberSerializer(member).data)

    def put(self, request, **kwargs):
        member_id = kwargs.get("member_id")
        if not member_id:
            return JsonResponse({}, status=404)

        try:
            member = TeamMember.objects.get(member_id=member_id)
        except TeamMember.DoesNotExist:
            return JsonResponse({}, status=404)

        input_json = json.loads(request.body)
        serializer = TeamMemberSerializer(member, data=input_json, partial=True)
        if not serializer.is_valid():
            return JsonResponse({"errors": serializer.errors})

        member = serializer.save()

        return JsonResponse(TeamMemberSerializer(member).data)

    def delete(self, request, **kwargs):
        member_id = kwargs.get("member_id")
        if not member_id:
            return JsonResponse({}, status=404)

        try:
            member = TeamMember.objects.get(member_id=member_id)
        except TeamMember.DoesNotExist:
            return JsonResponse({}, status=404)

        member.delete()
        return JsonResponse({}, status=204)
