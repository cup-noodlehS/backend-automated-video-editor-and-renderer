from tranches.utils.generic_api import GenericView
from organization.models import Organization, OrganizationMember, Credits
from organization.serializers import OrganizationSerializer, OrganizationMemberSerializer, CreditsSerializer


class OrganizationView(GenericView):
    queryset = Organization.objects.filter(archived=False)
    serializer_class = OrganizationSerializer


class OrganizationMemberView(GenericView):
    queryset = OrganizationMember.objects.all()
    serializer_class = OrganizationMemberSerializer


class CreditsView(GenericView):
    queryset = Credits.objects.all()
    serializer_class = CreditsSerializer