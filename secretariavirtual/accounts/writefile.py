from mailmerge import MailMerge
from .models import Feedback
from django.http.response import HttpResponse

class WriteAndDownload(object):

	def __init__(self, solicitation):

		self.template = "secretariavirtual/common-static/static/word-templates/modelo-requerimento-novo.docx"
		self.solicitation = solicitation
		self.document_name = 'requerimento-numero-'+solicitation.order+'.docx'

	def write_file(self):

		feedback_secretary = Feedback()
		feedback_lib = Feedback()
		feedback_fin = Feedback()
		feedback_coord = Feedback()
		feedback_napes = Feedback()
		feedback_dir = Feedback()
		feedback_caa = Feedback()
		
		for feedback in self.solicitation.feedbacks.all():

			if feedback.feedbacker.usuario.is_secretary:
				feedback_secretary = feedback

			elif feedback.feedbacker.usuario.is_library:
				feedback_lib = feedback

			elif feedback.feedbacker.usuario.is_finance:
				feedback_fin = feedback

			elif feedback.feedbacker.usuario.is_coordination:
				feedback_coord = feedback

			elif feedback.feedbacker.usuario.is_napes:
				feedback_napes = feedback

			elif feedback.feedbacker.usuario.is_director:
				feedback_dir = feedback

			elif feedback.feedbacker.usuario.is_caa:
				feedback_caa = feedback

		document = MailMerge(self.template)

		print(document.get_merge_fields())

		document.merge(
			order=self.solicitation.order,
			date=str(self.solicitation.created_at.day)+"/"+str(self.solicitation.created_at.month)+"/"+str(self.solicitation.created_at.year),
			name=self.solicitation.student.usuario.name,
			code=self.solicitation.code,
			email=self.solicitation.email,
			course=("Tecnólogo em gestão pública"),
			phone1=self.solicitation.phone1,
			phone2=self.solicitation.phone2,
			semester=self.solicitation.student_semester,
			classs=self.solicitation.classs,
			student_academic_situation=self.solicitation.student_academic_situation,
			solicitation=self.solicitation.solicitation,
			reason=self.solicitation.reason,
			secretary_feedback=feedback_secretary.feedback,
			coord_feedback=feedback_coord.feedback,
			dir_feedback=feedback_dir.feedback,
			napes_feedback=feedback_napes.feedback,
			lib_feedback=feedback_lib.feedback,
			finance_feedback=feedback_fin.feedback,
			caa_feedback=feedback_caa.feedback
	    )

		document.write("secretariavirtual/common-static/static/temporary-documents/"+self.document_name)

	def download(self):

		with open("secretariavirtual/common-static/static/temporary-documents/"+self.document_name, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/docx")
			response['Content-Disposition'] = 'inline; filename=' + self.document_name

		return response

