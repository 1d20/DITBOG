yes = "yes"
no = "no"

class Content_descriptors:
	cartoon_violence = no
	realistic_violence = no
	bad_language = no
	fear = no
	sexual_content = no
	drugs = no
	gambling_reference = no
	alcohol = no
	smoking = no
	discrimination = no

	def ToXML(self):
		xml = "<content-descriptors>"
		xml += "<cartoon-violence>" + self.cartoon_violence + "</cartoon-violence>"
		xml += "<realistic-violence>" + self.realistic_violence + "</realistic-violence>"
		xml += "<bad-language>" + self.bad_language + "</bad-language>"
		xml += "<fear>" + self.fear + "</fear>"
		xml += "<sexual-content>" + self.sexual_content + "</sexual-content>"
		xml += "<drugs>" + self.drugs + "</drugs>"
		xml += "<gambling-reference>" + self.gambling_reference + "</gambling-reference>"
		xml += "<alcohol>" + self.alcohol + "</alcohol>"
		xml += "<smoking>" + self.smoking + "</smoking>"
		xml += "<discrimination>" + self.discrimination + "</discrimination>"
		xml += "</content-descriptors>"
		return xml
		
class Included_activities:
	in_app_billing = no
	gambling = no
	advertising = yes
	user_generated_content = no
	user_to_user_communications = no
	account_creation = no
	personal_information_collection = no
	def ToXML(self):
		xml = "<included-activities>"
		xml += "<in-app-billing>" + self.in_app_billing + "</in-app-billing>"
		xml += "<gambling>" + self.gambling + "</gambling>"
		xml += "<advertising>" + self.advertising + "</advertising>"
		xml += "<user-generated-content>" + self.user_generated_content + "</user-generated-content>"
		xml += "<user-to-user-communications>" + self.user_to_user_communications + "</user-to-user-communications>"
		xml += "<account-creation>" + self.account_creation + "</account-creation>"
		xml += "<personal-information-collection>" + self.personal_information_collection + "</personal-information-collection>"
		xml += "</included-activities>"
		return xml

class Content_description:
	content_rating = 3
	content_descriptors = Content_descriptors()
	included_activities = Included_activities()
	def ToXML(self):
		xml = "<content-description>"
		xml += "<content-rating>" + str(self.content_rating) + "</content-rating>"
		xml += self.content_descriptors.ToXML()
		xml += self.included_activities.ToXML()
		xml += "</content-description>"
		return xml

class Apk_files:
	apk_file = ""
	def ToXML(self):
		return "<apk-files><apk-file>" + self.apk_file + "</apk-file></apk-files>"
		
class Categorization:
	type = ""
	category = ""
	subcategory = ""
	def ToXML(self):
		xml = "<categorization>"
		xml += "<type>" + self.type + "</type>"
		xml += "<category>" + self.category + "</category>"
		xml += "<subcategory>" + self.subcategory + "</subcategory>"
		xml += "</categorization>"
		return xml
		
class Consent:
	google_android_content_guidelines = yes
	us_export_laws = yes
	slideme_agreement = yes
	free_from_third_party_copytighted_content = yes
	import_export = yes
	def ToXML(self):
		xml = "<consent>"
		xml += "<google-android-content-guidelines>" + self.google_android_content_guidelines + "</google-android-content-guidelines>"
		xml += "<us-export-laws>" + self.us_export_laws + "</us-export-laws>"
		xml += "<slideme-agreement>" + self.slideme_agreement + "</slideme-agreement>"
		xml += "<free-from-third-party-copytighted-content>" + self.free_from_third_party_copytighted_content + "</free-from-third-party-copytighted-content>"
		xml += "<import-export>" + self.import_export + "</import-export>"
		xml += "</consent>"
		return xml
		
class Customer_support:
	phone = ""
	email = ""
	website = ""
	def ToXML(self):
		xml = "<customer-support>"
		xml += "<phone>" + self.phone + "</phone>"
		xml += "<email>" + self.email + "</email>"
		xml += "<website>" + self.website + "</website>"
		xml += "</customer-support>"
		return xml

class Images:
	icon = ""
	promo = ""
	screenshots = []
	def ToXML(self):
		xml = "<images>"
		xml += "<app-icon width=\"512\" height=\"512\">" + self.icon + "</app-icon>"
		xml += "<large-promo width=\"1024\" height=\"500\">" + self.promo + "</large-promo>"
		xml += "<screenshots>"
		i = 0
		for screen in self.screenshots:
			xml += "<screenshot width=\"480\" height=\"800\" index=\"" + (i+1) + "\">"
			xml += screenshots[i] + "</screenshot>"
			i+=1
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
		xml += "<title>" + self.title + "</title>"
		xml += "<keywords>" + self.keywords + "</keywords>"
		xml += "<short-description>" + self.short_description + "</short-description>"
		xml += "<full-description>" + self.full_description + "</full-description>"
		xml += "<features>"
		for feature in self.features:
			xml += "<feature>" + feature + "</feature>"
		xml += "</features>"
		xml += "</texts>"
		return xml
		
class Description:
	texts = Texts()
	images = Images()
	def ToXML(self):
		xml = "<description>"
		xml += self.texts.ToXML()
		xml += self.images.ToXML()
		xml += "</description>"
		return xml

class Description_localization:
	language = "ru"
	texts = Texts()
	def ToXML(self):
		xml = "<description-localization language=\"" + self.language + "\">"
		xml += self.texts.ToXML()
		xml += "</description-localization>"
		return xml

class DataMaster:
	version = "1"
	platform = "android"
	package = ""

	categorization = Categorization()
	description = Description()
	description_localizations = []
	content_description = Content_description()
	price = yes ##free="yes"
	apk_files = Apk_files()
	testing_instructions = "Not specified."
	consent = Consent()
	customer_support = Customer_support()

	def ToXML(self):
		xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><application-description-file version=\""+self.version+"\">"
		xml += "<application platform=\"" + self.platform + "\" package=\"" + self.package + "\">"

		xml += self.categorization.ToXML()
		xml += self.description.ToXML()

		for description_localization in self.description_localizations:
			xml += description_localization.ToXML()

		xml += self.content_description.ToXML()
		xml += "<price free=\"" + self.price + "\" />"
		xml += self.apk_files.ToXML()
		xml += "<testing-instructions>" + self.testing_instructions + "</testing-instructions>"
		xml += self.consent.ToXML()
		xml += self.customer_support.ToXML()

		xml += "</application></application-description-file>"

		return xml

		