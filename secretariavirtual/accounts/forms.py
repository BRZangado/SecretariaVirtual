from django import forms

CHOICES=[

        ('Aluno Especial','Aluno Especial'),
        ('Aproveitamento de Estudos','Aproveitamento de Estudos (anexar documentação)'),
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
         ('Outro','Outro (descrever na justificativa)')
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