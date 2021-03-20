from django.views import View
from django.http import JsonResponse
import json
from .models import TeamMember
from django.forms.models import model_to_dict


class MemberListView(View):
    def get(self, request):
        team_members = TeamMember.objects.values()
        return JsonResponse({"data": list(team_members)}, safe=False)

    def post(self, request):
        input_json = json.loads(request.body)
        new_member = TeamMember.objects.create(**input_json)
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

        return JsonResponse(model_to_dict(member))

    def put(self, request, **kwargs):
        member_id = kwargs.get("member_id")
        if not member_id:
            return JsonResponse({}, status=404)

        try:
            member = TeamMember.objects.get(member_id=member_id)
        except TeamMember.DoesNotExist:
            return JsonResponse({}, status=404)

        input_json = json.loads(request.body)
        for attr, val in input_json.items():
            setattr(member, attr, val)
        member.save()

        return JsonResponse(model_to_dict(member))

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
