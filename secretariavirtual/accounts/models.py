from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):

	feedbacker = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)

	feedback = models.CharField(
		('Parecer'),
		help_text=("Parecer de certo funcionário"),
		max_length=500,
		default=("Parecer não informado")
	)

	created_at = models.DateTimeField(
		('Data'),
    	help_text=("Data que o parecer foi criado"),
    	auto_now_add=True
    )

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return self.feedback

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("Parecer")
	    verbose_name_plural = ("Pareceres")
	    ordering = ('created_at',)


class Solicitation(models.Model):

	student = models.ForeignKey(
		User,
		help_text=("Estudante requerinte"),
		on_delete=models.CASCADE
	)

	email = models.CharField(
		('E-mail'),
		help_text=("E-mail do usuário"),
		max_length=50,
		default=("E-mail não informado")
	)

	classs = models.CharField(
		('Turma'),
		help_text=("Turma do Aluno"),
		max_length=10,
		default=("Turma não informada")
	)

	phone1 = models.CharField(
		('Telefone 1'),
		help_text=("Telefone principal do Aluno"),
		max_length=12,
		default=("Telefone não informado")
	)

	phone2 = models.CharField(
		('Telefone 2'),
		help_text=("Telefone secundário do Aluno"),
		max_length=12,
		default=("Telefone não informado")
	)

	order = models.CharField(
		('Processo'),
		unique=True,
		help_text=("Número do processo"),
		max_length=15
	)

	code = models.CharField(
		("Matrícula"),
        max_length=20,
        help_text=("Matrícula do Estudante"),
        default=('Matrícula não informada')
    )

	created_at = models.DateTimeField(
		('Data'),
    	help_text=("Data que a solicitação foi criada"),
    	auto_now_add=True
    )

	student_semester = models.CharField(
		('Período'),
		help_text=("Período do Estudante"),
		max_length=15
	)

	classs = models.CharField(
		('Turma'),
		help_text=("Turma do Estudante"),
		max_length=20,
		default=('turma não informada')
	)

	student_academic_situation = models.CharField(
		('Situação'),
		help_text=("Situação Acadêmica do Estudante"),
		max_length=50,
		default=('Situação acadêmica ainda não informada')
	)

	solicitation = models.CharField(
		('Solicitação'),
		help_text=("Solicitação"),
		max_length=100,
	)

	reason = models.CharField(
		('Justificativa'),
		help_text=("Justificativa da solicitação"),
		max_length=300,
	)

	status = models.CharField(
		('Status'),
		help_text=("Status da Solicitação"),
		max_length=30,
	)

	attachment_rg = models.FileField(
		('RG'),
		help_text=("RG Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/RG/',
		blank=True,
		null=True
	)

	attachment_voters_title = models.FileField(
		('Título de Eleitor'),
		help_text=("Título de Eleitor Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/Titulo-de-Eleitor/',
		blank=True,
		null=True
	)

	attachment_cpf = models.FileField(
		('CPF'),
		help_text=("CPF Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/CPF/',
		blank=True,
		null=True
	)

	attachment_proof_electoral_discharge = models.FileField(
		('Comprovante de Quitação Eleitoral'),
		help_text=("Comprovante de Quitação Eleitoral Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/comprovante-quitacao-eleitoral/',
		blank=True,
		null=True
	)

	attachment_reservist = models.FileField(
		('Título de Reservista'),
		help_text=("Título de Reservista Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/reservista/',
		blank=True,
		null=True
	)

	attachment_birth_marriage_certificate = models.FileField(
		('Certidão de casamento/Nascimento'),
		help_text=("Certidão de casamento/Nascimento Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/certidao-casamento-nascimento/',
		blank=True,
		null=True
	)

	attachment_highschool_certificate = models.FileField(
		('Certificado de Conclusão do Ensino Médio'),
		help_text=("Certificado de Conclusão do Ensino Médio Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/school-certificate/',
		blank=True,
		null=True
	)

	attachment_school_historic = models.FileField(
		('Histórico Escolar'),
		help_text=("Histórico Escolar Anexado pelo estudante"),
		upload_to='anexos/%Y/%m/school-historic/',
		blank=True,
		null=True
	)

	attachment_academic_bond_certificate = models.FileField(
		('Declaração de Vínculo Acadêmico'),
		help_text=("Declaração de Vínculo Acadêmico"),
		upload_to='anexos/%Y/%m/academic-bond-certificate/',
		blank=True,
		null=True
	)

	attachment_discipline_menu = models.FileField(
		('Ementas das disciplinas'),
		help_text=("Ementas das disciplinas cursadas na IES de origem"),
		upload_to='anexos/%Y/%m/discipline-menus/',
		blank=True,
		null=True
	)

	attachment_degree = models.FileField(
		('Diploma'),
		help_text=("Diploma da graduação"),
		upload_to='anexos/%Y/%m/degrees/',
		blank=True,
		null=True
	)

	feedbacks = models.ManyToManyField(
		Feedback,
		blank=True
	)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return self.order

	class Meta:
	    """
	    Some information about Solicitation class.
	    """
	    verbose_name = ("Requerimento")
	    verbose_name_plural = ("Requerimentos")
	    ordering = ('created_at',)


class Usuario(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE
	)

	name = models.CharField(
		('Nome'),
		help_text=("Nome completo do usuário"),
		max_length=150
	)

	is_staff = models.BooleanField(
		('Is Staff?'),
		help_text=("Verify if the user is a staff."),
		default=False
	)

	is_student = models.BooleanField(
		('Is Student?'),
    	help_text=("Verificar se o usuário é um aluno"),
    	default=False
    )

	is_secretary = models.BooleanField(
		('Is Secretary?'),
		help_text=("Verificar se o usuário é um Secretaria Acadêmica"),
		default=False
	)

	is_library = models.BooleanField(
		('Is Librarian?'),
		help_text=("Verificar se o usuário é um Bibliotecário"),
		default=False
	)

	is_finance = models.BooleanField(
		('Is Finance?'),
		help_text=("Verificar se o usuário é do Financeiro"),
		default=False
	)

	is_coordination = models.BooleanField(
		('Is Coordination'),
		help_text=("Verificar se o usuário é da Coordenação"),
		default=False
	)

	is_napes = models.BooleanField(
		('Is NAPES?'),
		help_text=("Verificar se o usuário é NAPES"),
		default=False
	)

	is_director = models.BooleanField(
		('Is Director?'),
		help_text=("Verificar se o usuário é Diretor Acadêmico"),
		default=False
	)

	is_caa = models.BooleanField(
		('Is CAA?'),
		help_text=("Verificar se o usuário é da Central de Atendimento ao Aluno"),
		default=False
	)

	created_at = models.DateTimeField(
		('Created at'),
    	help_text=("Date that the user is created."),
    	auto_now_add=True
    )

	updated_at = models.DateTimeField(
		('Updated at'),
		help_text=("Date that the user is updated."),
		auto_now=True
	)

	solicitations = models.ManyToManyField(
		Solicitation,
		blank=True
	)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return self.name

	def get_full_name(self):
	    """
	    Used to get the user full name.
	    """
	    return self.name

	class Meta:
	    """
	    Some information about user class.
	    """
	    verbose_name = ("Usuário")
	    verbose_name_plural = ("Usuários")
	    ordering = ('created_at',)