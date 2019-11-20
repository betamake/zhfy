from django.db import models
import sys,os
sys.path.append(os.path.realpath('.'))
from user.models import User
# Create your models here.
class YulianNewCase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #base_massage
    type_of_applicant = models.CharField(max_length=256)
    case_involving = models.CharField(max_length=256)
    need_for_property_preservation = models.CharField(max_length=256)
    court = models.CharField(max_length=256)
    subject_amount = models.CharField(max_length=256)
    subject_matter = models.CharField(max_length=256)
    subject_behavior = models.CharField(max_length=256)
    register_reason = models.CharField(max_length=256)
    register_date = models.CharField(max_length=256)
    #litigant_massage/plaintiff/nature_person
    pnp_name =models.CharField(max_length=256)
    pnp_gender =models.CharField(max_length=256)
    pnp_id_card_type =models.CharField(max_length=256)
    pnp_id_card_num =models.CharField(max_length=256)
    pnp_telephone =models.CharField(max_length=256)
    pnp_address_now_living =models.CharField(max_length=256)
    pnp_address_always_living =models.CharField(max_length=256)
    pnp_address_register =models.CharField(max_length=256)
    pnp_address_post =models.CharField(max_length=256)
    pnp_first_agent_type =models.CharField(max_length=256)
    pnp_first_agent_name =models.CharField(max_length=256)
    pnp_first_agent_telephone =models.CharField(max_length=256)
    pnp_first_agent_id_card_type =models.CharField(max_length=256)
    pnp_first_agent_id_card_num =models.CharField(max_length=256)
    pnp_first_agent_lawyer_license_num =models.CharField(max_length=256)
    pnp_second_agent_type =models.CharField(max_length=256)
    pnp_second_agent_name =models.CharField(max_length=256)
    pnp_second_agent_telephone =models.CharField(max_length=256)
    pnp_second_agent_id_card_type =models.CharField(max_length=256)
    pnp_second_agent_id_card_num =models.CharField(max_length=256)
    pnp_second_agent_lawyer_license_num =models.CharField(max_length=256)
    # litigant_massage/plaintiff/legal_person
    plp_name = models.CharField(max_length=256)
    plaintiff_legal_representative_name = models.CharField(max_length=256)
    plp_id_card_type = models.CharField(max_length=256)
    plp_id_card_num = models.CharField(max_length=256)
    plp_representative_telephone = models.CharField(max_length=256)
    plp_representative_id_card_num = models.CharField(max_length=256)
    plp_address_register = models.CharField(max_length=256)
    plp_address_post = models.CharField(max_length=256)
    plp_first_agent_type = models.CharField(max_length=256)
    plp_first_agent_name = models.CharField(max_length=256)
    plp_first_agent_telephone = models.CharField(max_length=256)
    plp_first_agent_id_card_type = models.CharField(max_length=256)
    plp_first_agent_id_card_num = models.CharField(max_length=256)
    plp_first_agent_lawyer_license_num = models.CharField(max_length=256)
    plp_second_agent_type = models.CharField(max_length=256)
    plp_second_agent_name = models.CharField(max_length=256)
    plp_second_agent_telephone = models.CharField(max_length=256)
    plp_second_agent_id_card_type = models.CharField(max_length=256)
    plp_second_agent_id_card_num = models.CharField(max_length=256)
    plp_second_agent_lawyer_license_num = models.CharField(max_length=256)
    # litigant_massage/plaintiff/unincorporated_organization
    puo_name = models.CharField(max_length=256)
    puo_person_in_charge_name = models.CharField(max_length=256)
    puo_id_card_type = models.CharField(max_length=256)
    puo_id_card_num = models.CharField(max_length=256)
    puo_person_in_charge_telephone = models.CharField(max_length=256)
    puo_person_in_charge_id_card_num = models.CharField(max_length=256)
    puo_address_contact = models.CharField(max_length=256)
    puo_address_post = models.CharField(max_length=256)
    puo_first_agent_type = models.CharField(max_length=256)
    puo_first_agent_name = models.CharField(max_length=256)
    puo_first_agent_telephone = models.CharField(max_length=256)
    puo_first_agent_id_card_type = models.CharField(max_length=256)
    puo_first_agent_id_card_num = models.CharField(max_length=256)
    puo_first_agent_lawyer_license_num = models.CharField(max_length=256)
    puo_second_agent_type = models.CharField(max_length=256)
    puo_second_agent_name = models.CharField(max_length=256)
    puo_second_agent_telephone = models.CharField(max_length=256)
    puo_second_agent_id_card_type = models.CharField(max_length=256)
    puo_second_agent_id_card_num = models.CharField(max_length=256)
    puo_second_agent_lawyer_license_num = models.CharField(max_length=256)
    # litigant_massage/defendant/nature_person
    dnp_name = models.CharField(max_length=256)
    dnp_gender = models.CharField(max_length=256)
    dnp_id_card_type = models.CharField(max_length=256)
    dnp_id_card_num = models.CharField(max_length=256)
    dnp_telephone = models.CharField(max_length=256)
    dnp_address_now_living = models.CharField(max_length=256)
    dnp_address_always_living = models.CharField(max_length=256)
    dnp_address_register = models.CharField(max_length=256)
    dnp_address_post = models.CharField(max_length=256)
    dnp_first_agent_type = models.CharField(max_length=256)
    dnp_first_agent_name = models.CharField(max_length=256)
    dnp_first_agent_telephone = models.CharField(max_length=256)
    dnp_first_agent_id_card_type = models.CharField(max_length=256)
    dnp_first_agent_id_card_num = models.CharField(max_length=256)
    dnp_first_agent_lawyer_license_num = models.CharField(max_length=256)
    dnp_second_agent_type = models.CharField(max_length=256)
    dnp_second_agent_name = models.CharField(max_length=256)
    dnp_second_agent_telephone = models.CharField(max_length=256)
    dnp_second_agent_id_card_type = models.CharField(max_length=256)
    dnp_second_agent_id_card_num = models.CharField(max_length=256)
    dnp_second_agent_lawyer_license_num = models.CharField(max_length=256)
    # litigant_massage/defendant/legal_person
    dlp_name = models.CharField(max_length=256)
    dlp_representative_name = models.CharField(max_length=256)
    dlp_id_card_type = models.CharField(max_length=256)
    dlp_id_card_num = models.CharField(max_length=256)
    dlp_representative_telephone = models.CharField(max_length=256)
    dlp_representative_id_card_num = models.CharField(max_length=256)
    dlp_address_register = models.CharField(max_length=256)
    dlp_address_post = models.CharField(max_length=256)
    dlp_first_agent_type = models.CharField(max_length=256)
    dlp_first_agent_name = models.CharField(max_length=256)
    dlp_first_agent_telephone = models.CharField(max_length=256)
    dlp_first_agent_id_card_type = models.CharField(max_length=256)
    dlp_first_agent_id_card_num = models.CharField(max_length=256)
    dlp_first_agent_lawyer_license_num = models.CharField(max_length=256)
    dlp_second_agent_type = models.CharField(max_length=256)
    dlp_second_agent_name = models.CharField(max_length=256)
    dlp_second_agent_telephone = models.CharField(max_length=256)
    dlp_second_agent_id_card_type = models.CharField(max_length=256)
    dlp_second_agent_id_card_num = models.CharField(max_length=256)
    dlp_second_agent_lawyer_license_num = models.CharField(max_length=256)
    # litigant_massage/defendant/legal_person
    duo_name = models.CharField(max_length=256)
    duo_person_in_charge_name = models.CharField(max_length=256)
    duo_id_card_type = models.CharField(max_length=256)
    duo_id_card_num = models.CharField(max_length=256)
    duo_person_in_charge_telephone = models.CharField(max_length=256)
    duo_person_in_charge_id_card_num = models.CharField(max_length=256)
    duo_address_contact = models.CharField(max_length=256)
    duo_address_post = models.CharField(max_length=256)
    duo_first_agent_type = models.CharField(max_length=256)
    duo_first_agent_name = models.CharField(max_length=256)
    duo_first_agent_telephone = models.CharField(max_length=256)
    duo_first_agent_id_card_type = models.CharField(max_length=256)
    duo_first_agent_id_card_num = models.CharField(max_length=256)
    duo_first_agent_lawyer_license_num = models.CharField(max_length=256)
    duo_second_agent_type = models.CharField(max_length=256)
    duo_second_agent_name = models.CharField(max_length=256)
    duo_second_agent_telephone = models.CharField(max_length=256)
    duo_second_agent_id_card_type = models.CharField(max_length=256)
    duo_second_agent_id_card_num = models.CharField(max_length=256)
    duo_second_agent_lawyer_license_num = models.CharField(max_length=256)

    # litigant_massage/third_party/nature_person
    tnp_name = models.CharField(max_length=256)
    tnp_gender = models.CharField(max_length=256)
    tnp_id_card_type = models.CharField(max_length=256)
    tnp_id_card_num = models.CharField(max_length=256)
    tnp_telephone = models.CharField(max_length=256)
    tnp_address_now_living = models.CharField(max_length=256)
    tnp_address_always_living = models.CharField(max_length=256)
    tnp_address_register = models.CharField(max_length=256)
    tnp_address_post = models.CharField(max_length=256)
    tnp_first_agent_type = models.CharField(max_length=256)
    tnp_first_agent_name = models.CharField(max_length=256)
    tnp_first_agent_telephone = models.CharField(max_length=256)
    tnp_first_agent_id_card_type = models.CharField(max_length=256)
    tnp_first_agent_id_card_num = models.CharField(max_length=256)
    tnp_first_agent_lawyer_license_num = models.CharField(max_length=256)
    tnp_second_agent_type = models.CharField(max_length=256)
    tnp_second_agent_name = models.CharField(max_length=256)
    tnp_second_agent_telephone = models.CharField(max_length=256)
    tnp_second_agent_id_card_type = models.CharField(max_length=256)
    tnp_second_agent_id_card_num = models.CharField(max_length=256)
    tnp_second_agent_lawyer_license_num = models.CharField(max_length=256)
    # litigant_massage/third_party/legal_person
    tlp_name = models.CharField(max_length=256)
    tlp_representative_name = models.CharField(max_length=256)
    tlp_id_card_type = models.CharField(max_length=256)
    tlp_id_card_num = models.CharField(max_length=256)
    tlp_representative_telephone = models.CharField(max_length=256)
    tlp_representative_id_card_num = models.CharField(max_length=256)
    tlp_address_register = models.CharField(max_length=256)
    tlp_address_post = models.CharField(max_length=256)
    tlp_first_agent_type = models.CharField(max_length=256)
    tlp_first_agent_name = models.CharField(max_length=256)
    tlp_first_agent_telephone = models.CharField(max_length=256)
    tlp_first_agent_id_card_type = models.CharField(max_length=256)
    tlp_first_agent_id_card_num = models.CharField(max_length=256)
    tlp_first_agent_lawyer_license_num = models.CharField(max_length=256)
    tlp_second_agent_type = models.CharField(max_length=256)
    tlp_second_agent_name = models.CharField(max_length=256)
    tlp_second_agent_telephone = models.CharField(max_length=256)
    tlp_second_agent_id_card_type = models.CharField(max_length=256)
    tlp_second_agent_id_card_num = models.CharField(max_length=256)
    tlp_second_agent_lawyer_license_num = models.CharField(max_length=256)
    # litigant_massage/third_party/unincorporated_organization
    tuo_name = models.CharField(max_length=256)
    tuo_person_in_charge_name = models.CharField(max_length=256)
    tuo_id_card_type = models.CharField(max_length=256)
    tuo_id_card_num = models.CharField(max_length=256)
    tuo_person_in_charge_telephone = models.CharField(max_length=256)
    tuo_person_in_charge_id_card_num = models.CharField(max_length=256)
    tuo_address_contact = models.CharField(max_length=256)
    tuo_address_post = models.CharField(max_length=256)
    tuo_first_agent_type = models.CharField(max_length=256)
    tuo_first_agent_name = models.CharField(max_length=256)
    tuo_first_agent_telephone = models.CharField(max_length=256)
    tuo_first_agent_id_card_type = models.CharField(max_length=256)
    tuo_first_agent_id_card_num = models.CharField(max_length=256)
    tuo_first_agent_lawyer_license_num = models.CharField(max_length=256)
    tuo_second_agent_type = models.CharField(max_length=256)
    tuo_second_agent_name = models.CharField(max_length=256)
    tuo_second_agent_telephone = models.CharField(max_length=256)
    tuo_second_agent_id_card_type = models.CharField(max_length=256)
    tuo_second_agent_id_card_num = models.CharField(max_length=256)
    tuo_second_agent_lawyer_license_num = models.CharField(max_length=256)

    #litigation_information
    litigation_request = models.CharField(max_length=256)
    fact_and_reason = models.CharField(max_length=256)

class AllFaYuan(models.Model):
    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    shangji_fayuan = models.CharField(max_length=256)
    fayuan_jibie = models.CharField(max_length=256)
    xiaxia_fayuan_number = models.CharField(max_length=256)
    beizhu = models.CharField(max_length=256)