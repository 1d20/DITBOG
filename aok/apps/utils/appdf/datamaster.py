from enum import Enum

class YesNo(Enum):
	yes = "yes"
	no = "no"

class Content_descriptors:
	cartoon_violence = YesNo.no
	realistic_violence = YesNo.no
	bad_language = YesNo.no
	fear = YesNo.no
	sexual_content = YesNo.no
	drugs = YesNo.no
	gambling_reference = YesNo.no
	alcohol = YesNo.no
	smoking = YesNo.no
	discrimination = YesNo.no

	def ToXML(self):
		xml = "<content-descriptors>"
		xml += "<cartoon-violence>" + cartoon_violence + "</cartoon-violence>"
		xml += "<realistic-violence>" + realistic_violence + "</realistic-violence>"
		xml += "<bad-language>" + bad_language + "</bad-language>"
		xml += "<fear>" + fear + "</fear>"
		xml += "<sexual-content>" + sexual_content + "</sexual-content>"
		xml += "<drugs>" + drugs + "</drugs>"
		xml += "<gambling-reference>" + gambling_reference + "</gambling-reference>"
		xml += "<alcohol>" + alcohol + "</alcohol>"
		xml += "<smoking>" + smoking + "</smoking>"
		xml += "<discrimination>" + discrimination + "</discrimination>"
		xml += "</content-descriptors>"
		return xml
		
class Included_activities:
	in_app_billing = YesNo.no
	gambling = YesNo.no
	advertising = YesNo.yes
	user_generated_content = YesNo.no
	user_to_user_communications = YesNo.no
	account_creation = YesNo.no
	personal_information_collection = YesNo.no
	def ToXML(self):
		xml = "<included-activities>"
		xml += "<in-app-billing>" + in_app_billing + "</in-app-billing>"
		xml += "<gambling>" + gambling + "</gambling>"
		xml += "<advertising>" + advertising + "</advertising>"
		xml += "<user-generated-content>" + user_generated_content + "</user-generated-content>"
		xml += "<user-to-user-communications>" + user_to_user_communications + "</user-to-user-communications>"
		xml += "<account-creation>" + account_creation + "</account-creation>"
		xml += "<personal-information-collection>" + personal_information_collection + "</personal-information-collection>"
		xml += "</included-activities>"
		return xml

class Сontent_description:
	content_rating = 3
	content_descriptors = Content_descriptors()
	included_activities = Included_activities()
	def ToXML(self):
		xml = "<content-description>"
		xml += "<content-rating>" + content_rating + "</content-rating>"
		xml += content_descriptors.ToXML()
		xml += included_activities.ToXML()
		xml += "</content-description>"
		return xml

class Apk_files:
	apk_file = ""
	def ToXML(self):
		return "<apk-files><apk-file>" + apk_file + "</apk-file></apk-files>"
		
class Categorization:
	type = ""
	category = ""
	subcategory = ""
	def ToXML(self):
		xml = "<categorization>"
		xml += "<type>" + type + "</type>"
		xml += "<category>" + category + "</category>"
		xml += "<subcategory>" + subcategory + "</subcategory>"
		xml += "</categorization>"
		return xml
		
class Consent:
	google_android_content_guidelines = YesNo.yes
	us_export_laws = YesNo.yes
	slideme_agreement = YesNo.yes
	free_from_third_party_copytighted_content = YesNo.yes
	import_export = YesNo.yes
	def ToXML(self):
		xml = "<consent>"
		xml += "<google-android-content-guidelines>" + google_android_content_guidelines + "</google-android-content-guidelines>"
		xml += "<us-export-laws>" + us_export_laws + "</us-export-laws>"
		xml += "<slideme-agreement>" + slideme_agreement + "</slideme-agreement>"
		xml += "<free-from-third-party-copytighted-content>" + free_from_third_party_copytighted_content + "</free-from-third-party-copytighted-content>"
		xml += "<import-export>" + import_export + "</import-export>"
		xml += "</consent>"
		return xml
		
class Customer_support:
	phone = ""
	email = ""
	website = ""
	def ToXML(self):
		xml = "<customer-support>"
		xml += "<phone>" + phone + "</phone>"
		xml += "<email>" + email + "</email>"
		xml += "<website>" + website + "</website>"
		xml += "</customer-support>"
		return xml

class Images:
	icon = ""
	promo = ""
	screenshots = []
	def ToXML(self):
		xml = "<images>"
		xml += "<app-icon width=\"512\" height=\"512\">" + icon + "</app-icon>"
		xml += "<large-promo width=\"1024\" height=\"500\">" + promo + "</large-promo>"
		xml += "<screenshots>"
		i = 0
		for screen in screenshots:
			xml += "<screenshot width=\"480\" height=\"800\" index=\"" + (i+1) + "\">"
			xml += screenshots[i] + "</screenshot>"
			i++
		xml += "</screenshots>"
		xml += "</images>"
		return xml

class Texts:
	title = ""
	keywords = ""
	short_description = ""
	full_description = ""
	features = []
	def ToXML(self):
		xml = "<texts>"
		xml += "<title>" + title + "</title>"
		xml += "<keywords>" + keywords + "</keywords>"
		xml += "<short-description>" + short_description + "</short-description>"
		xml += "<full-description>" + full_description + "</full-description>"
		xml += "<features>"
		for feature in features:
			xml += "<feature>" + feature + "</feature>"
		xml += "</features>"
		xml += "</texts>"
		return xml
		
class Description:
	texts = Texts()
	images = Images()
	def ToXML(self):
		xml = "<description>"
		xml += texts.ToXML()
		xml += images.ToXML()
		xml += "</description>"
		return xml

class Description_localization:
	language = "ru"
	texts = Texts()
	def ToXML(self):
		xml = "<description-localization language=\"" + language + "\">"
		xml += texts.ToXML()
		xml += "</description-localization>"
		return xml

class DataMaster:
	version = "1"
	platform = "android"
	package = ""

	categorization = Categorization()
	description = Description()
	description_localizations = []
	content_description = Сontent_description()
	price = YesNo.yes //free="yes"
	apk_files = Apk_files()
	testing_instructions = "Not specified."
	consent = Consent()
	customer_support = Customer_support()
	def ToXML(self):
		xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><application-description-file version=\""+version+"\">"
		xml += "<application platform=\"" + platform + "\" package=\"" + package + "\">"

		xml += categorization.ToXML()
		xml += description.ToXML()

		for description_localization in description_localizations:
			xml += description_localization.ToXML()

		xml += content_description.ToXML()
		xml += "<price free=\"" + price + "\" />"
		xml += apk_files.ToXML()
		xml += "<testing-instructions>" + testing_instructions + "</testing-instructions>"
		xml += consent.ToXML()
		xml += customer_support.ToXML()

		xml += "</application></application-description-file>"

		return xml

		