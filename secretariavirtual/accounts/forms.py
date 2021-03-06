from django import forms

CHOICES=[

        ('Aluno Especial','Aluno Especial'),
        ('Aproveitamento de Estudos (Ingresso por Transferência)','Aproveitamento de Estudos (Ingresso por Transferência) (anexar documentação)'),
        ('Aproveitamento de Estudos (Ingresso por Segunda Graduação)','Aproveitamento de Estudos (Ingresso por Segunda Graduação) (anexar documentação)'),
        ('Cancelamento Matrícula','Cancelamento Matrícula***'),
         ('Colação de Grau Coletiva','Colação de Grau Coletiva**'),
         ('Colação de Grau Especial','Colação de Grau Especial**'),
         ('Declaração de Conclusão de Curso','Declaração de Conclusão de Curso (Escrever na justificativa se é 1ª via ou 2ª via)'),
         ('Declaração de Escolaridade','Declaração de Escolaridade (Escrever na justificativa se é 1ª via ou 2ª via)'),
         ('Histórico Escolar','Histórico Escolar*'),
         ('Mudança de Turno ou Turma','Mudança de Turno ou Turma'),
         ('Programas das disciplinas cursadas','Programas das disciplinas cursadas* (Descrever motivo na justificativa)'),
         ('Revisão de Frequencia','Revisão de Frequencia'),
         ('Reabertura de Matrícula/Reingresso','Reabertura de Matrícula/Reingresso'),
         ('Revisão de Notas','Revisão de Notas'),
         ('Revisão de Notas','Trancamento de Matrícula***'),
         ('Solicitção de 2ª chamada de prova','Solicitção de 2ª chamada de prova*'),
         ('Outro','Outro (descrever na justificativa)'),
         ('Declaração de vinculo acadêmico', 'Declaração de vinculo acadêmico'),
         ('Declaração para aquisição de passe estudantil','Declaração para aquisição de passe estudantil'),
         ('Solicitação do Diploma','Solicitação do Diploma (anexar documentação) ')
]

class StudentSolicitationForm(forms.Form):

    email = forms.CharField(
        max_length=35,
        label=("E-mail"),
        help_text=("Digite seu email")
    )
    course = forms.CharField(
        max_length=35,
        label=("Curso"),
        help_text=("Curso")
    )
    semester = forms.CharField(
        max_length=35,
        label=("Período"),
        help_text=("Período que está cursando")
    )
    classs = forms.CharField(
        max_length=35,
        label=("Turma"),
        help_text=("Sua turma")
    )
    code = forms.CharField(
        max_length=20,
        label=("Matrícula"),
        help_text=("Digite sua matrícula"),
        required=True,
    )
    phone_one = forms.CharField(
        max_length=20,
        label=("Telefone"),
        help_text=("Digite seu telefone principal"),
    )
    phone_two = forms.CharField(
        max_length=20,
        label=("Telefone secundário"),
        help_text=("Digite seu telefone secundário"),
    )
    solicitations = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    justification = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        label=("Justificativa"),
        help_text=("Digite a justificativa da solicitação"),
    )

    attachment_rg = forms.FileField(
        required=False
    )

    attachment_voters_title = forms.FileField(
        required=False
    )

    attachment_cpf = forms.FileField(
        required=False
    )

    attachment_proof_electoral_discharge = forms.FileField(
        required=False
    )

    attachment_reservist = forms.FileField(
        required=False
    )

    attachment_birth_marriage_certificate = forms.FileField(
        required=False
    )

    attachment_highschool_certificate = forms.FileField(
        required=False
    )

    attachment_school_historic = forms.FileField(
        required=False
    )

    attachment_academic_bond_certificate = forms.FileField(
        required=False
    )

    attachment_discipline_menu = forms.FileField(
        required=False
    )

    attachment_degree = forms.FileField(
        required=False
    )


class GenericFeedbackForm(forms.Form):

    feedback = forms.CharField(
        label=("Parecer"),
        max_length=500,
        widget=forms.Textarea,
    )
        

class SecretarySolicitationForm(GenericFeedbackForm):

    student_academic_situation = forms.CharField(
        label=("Situação Acadêmica"),
        help_text=("Situação Acadêmica do Estudante"),
        max_length=50,
        required=False
    )