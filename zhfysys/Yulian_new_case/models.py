from django.db import models
import sys,os
sys.path.append(os.path.realpath('.'))
from user.models import User
# Create your models here.
class YulianNewCase(models.Model):
    """选择法院和案件类型"""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type_of_anJian = models.CharField(max_length=256,verbose_name="案件类型")
    court = models.CharField(max_length=256,verbose_name="经办法院")
    register_date = models.CharField(max_length=256,verbose_name="立案日期")

    """申请人信息"""
    type_of_applicant = models.CharField(max_length=256,verbose_name="申请人信息")
    case_involving = models.CharField(max_length=256,verbose_name="案件涉及")
    need_for_property_preservation = models.CharField(max_length=256,verbose_name='是否需要财产保全')
    subject_amount = models.CharField(max_length=256,verbose_name='标的金额')
    subject_matter = models.CharField(max_length=256,verbose_name='标的物')
    subject_behavior = models.CharField(max_length=256)
    register_reason = models.CharField(max_length=256)
    #litigation_information
    litigation_request = models.CharField(max_length=256)
    fact_and_reason = models.CharField(max_length=256)

    def __str__(self):
        return self.type_of_applicant


class PnpNaturePerson(models.Model):
    """litigant_massage/plaintiff/nature_person 当事人原告信息"""
    yu_lian_new_case = models.ForeignKey(YulianNewCase,on_delete=models.CASCADE)
    name =models.CharField(max_length=256)
    gender =models.CharField(max_length=256)
    id_card_type =models.CharField(max_length=256)
    id_card_num =models.CharField(max_length=256)
    telephone =models.CharField(max_length=256)
    address_now_living =models.CharField(max_length=256)
    address_always_living =models.CharField(max_length=256)
    address_register =models.CharField(max_length=256)
    address_post =models.CharField(max_length=256)
    first_agent_type =models.CharField(max_length=256)
    first_agent_name =models.CharField(max_length=256)
    first_agent_telephone =models.CharField(max_length=256)
    first_agent_id_card_type =models.CharField(max_length=256)
    first_agent_id_card_num =models.CharField(max_length=256)
    first_agent_lawyer_license_num =models.CharField(max_length=256)
    second_agent_type =models.CharField(max_length=256)
    second_agent_name =models.CharField(max_length=256)
    second_agent_telephone =models.CharField(max_length=256)
    second_agent_id_card_type =models.CharField(max_length=256)
    second_agent_id_card_num =models.CharField(max_length=256)
    second_agent_lawyer_license_num =models.CharField(max_length=256)

    def __str__(self):
        return self.name
    # litigant_massage/plaintiff/legal_person

class PlpLegalPerson(models.Model):

    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    plaintiff_legal_representative_name = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    representative_telephone = models.CharField(max_length=256)
    representative_id_card_num = models.CharField(max_length=256)
    address_register = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # litigant_massage/plaintiff/unincorporated_organization
class PuoUnincorporatedOrganization(models.Model):

    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    person_in_charge_name = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    person_in_charge_telephone = models.CharField(max_length=256)
    person_in_charge_id_card_num = models.CharField(max_length=256)
    address_contact = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)
    def __str__(self):
        return self.name

    # litigant_massage/defendant/nature_person

class DnpNaturePerson(models.Model):
    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    telephone = models.CharField(max_length=256)
    address_now_living = models.CharField(max_length=256)
    address_always_living = models.CharField(max_length=256)
    address_register = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)
    # litigant_massage/defendant/legal_person
    def __str__(self):
        return self.name

class DlpLegalPerson(models.Model):
    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    representative_name = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    representative_telephone = models.CharField(max_length=256)
    representative_id_card_num = models.CharField(max_length=256)
    address_register = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    # litigant_massage/defendant/legal_person

class DuoLegalPerson(models.Model):
    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    person_in_charge_name = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    person_in_charge_telephone = models.CharField(max_length=256)
    person_in_charge_id_card_num = models.CharField(max_length=256)
    address_contact = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # litigant_massage/third_party/nature_person
class TnpNaturePerson(models.Model):
    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    telephone = models.CharField(max_length=256)
    address_now_living = models.CharField(max_length=256)
    address_always_living = models.CharField(max_length=256)
    address_register = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    # litigant_massage/third_party/legal_person

class TlpLegalPerson(models.Model):
    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    representative_name = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    representative_telephone = models.CharField(max_length=256)
    representative_id_card_num = models.CharField(max_length=256)
    address_register = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    # litigant_massage/third_party/unincorporated_organization

class TuoUnincorporatedOrganization(models.Model):
    yu_lian_new_case = models.ForeignKey(YulianNewCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    person_in_charge_name = models.CharField(max_length=256)
    id_card_type = models.CharField(max_length=256)
    id_card_num = models.CharField(max_length=256)
    person_in_charge_telephone = models.CharField(max_length=256)
    person_in_charge_id_card_num = models.CharField(max_length=256)
    address_contact = models.CharField(max_length=256)
    address_post = models.CharField(max_length=256)
    first_agent_type = models.CharField(max_length=256)
    first_agent_name = models.CharField(max_length=256)
    first_agent_telephone = models.CharField(max_length=256)
    first_agent_id_card_type = models.CharField(max_length=256)
    first_agent_id_card_num = models.CharField(max_length=256)
    first_agent_lawyer_license_num = models.CharField(max_length=256)
    second_agent_type = models.CharField(max_length=256)
    second_agent_name = models.CharField(max_length=256)
    second_agent_telephone = models.CharField(max_length=256)
    second_agent_id_card_type = models.CharField(max_length=256)
    second_agent_id_card_num = models.CharField(max_length=256)
    second_agent_lawyer_license_num = models.CharField(max_length=256)

    def __str__(self):
        return self.name

