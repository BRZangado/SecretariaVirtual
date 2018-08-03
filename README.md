# SecretariaVirtual
Django-based file and protocols transfer system across multiple college staff and students.

Sistema baseado em Django de tranferência de arquivos e solicitações entre vários estudantes e funcionários da Faculdade.

# Documento de visão do software

## Papéis

* Product Owner: Faculdade Anasps
* Scrum Master e Engenheiro de Software: Bruno Rodrigues Santos
* Principais Usuários:
	
	* Alunos
	* Secretaria Acadêmica
	* Coordenadores
	* Gerente Financeiro
	* Bibliotecário
	* Direção Acadêmica

## Backlog do produto (Em formato US)

* Eu como aluno, quero poder criar uma solicitação acadêmica de múltiplos fatores em ambiente virtual
* Eu como aluno, quero poder acompanhar o status da minha solicitação.
* Eu como secretária acadêmica, quero atender a demanda de solicitações acadêmicas em ambiente virtual
* Eu como secretária acadêmica, quero visualizar o formulário de requisição preenchidos pelos alunos
* Eu como secretária acadêmica, preciso encaminhas os formulários para o restante dos funcionários da Faculdade
* Eu como Coordenador, preciso preencher um parecer sobre a solicitação acadêmica do aluno
* Eu como Gerente Financeiro, preciso preencher um parecer sobre a solicitação acadêmica do aluno
* Eu como Bibliotecário, preciso preencher um parecer sobre a solicitação acadêmica do aluno
* Eu como Direção Acadêmica, preciso preencher um parecer sobre a solicitação acadêmica do aluno


## Arquitetura (v0.1)

* Padrão Arquitetural
  * MVT - Padrão Arquitetural usado pelo framework Django
  
  ![](https://mdn.mozillademos.org/files/13931/basic-django.png)

* MER

  ![](https://i.imgur.com/rotiFsL.jpg)
