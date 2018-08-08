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
		max_length=30,
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