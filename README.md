# SecretariaVirtual
Django-based file and protocols transfer system across multiple college staff and students.

Sistema baseado em Django de tranferência de arquivos e solicitações entre vários estudantes e funcionários da Faculdade.

## Escopo

* Suprir a demanda de requisições e solicitações acadêmicas de forma totalmente virtual,
poupando o aluno de se locomover presencialmente e aumentando a mobilidade e rapidez das tranferências de arquivos entre os funcionários da Faculdade.

## Ambiente do Usuário
O sistema será utilizado nos browsers Google Chrome, Safari, Internet Explorer, Firefox, Opera e Edge.

## Papéis

* Product Owner: Secretaria Acadêmica Faculdade Anasps
* Scrum Master e Engenheiro de Software: Bruno Rodrigues Santos
* Principais Usuários:
	
	* Alunos
	* Secretaria Acadêmica
	* Coordenadores
	* Gerente Financeiro
	* Bibliotecário
	* Direção Acadêmica

## Backlog do produto

### User Storys

* Eu como aluno, quero poder criar uma solicitação acadêmica de múltiplos fatores em ambiente virtual
* Eu como aluno, quero poder acompanhar o status da minha solicitação.
* Eu como secretária acadêmica, quero atender a demanda de solicitações acadêmicas em ambiente virtual
* Eu como secretária acadêmica, quero visualizar o formulário de requisição preenchidos pelos alunos
* Eu como secretária acadêmica, preciso encaminhar os formulários para o restante dos funcionários da Faculdade
* Eu como secretária acadêmica, preciso ter a opção de encerrar um requerimento
* Eu como secretária acadêmica, preciso guardar os requerimentos encerrados em pastas de acordo com o ano do requerimento
* Eu como secretária acadêmica, quero poder baixar um arquivo docx sobre as requisições encerradas
* Eu como secretária acadêmica, quero poder reabrir um requerimento caso seja necessário
* Eu como Coordenador, preciso preencher um parecer sobre a solicitação acadêmica do aluno
* Eu como Gerente Financeiro, preciso preencher um parecer sobre a solicitação acadêmica do aluno
* Eu como Bibliotecário, preciso preencher um parecer sobre a solicitação acadêmica do aluno
* Eu como Direção Acadêmica, preciso preencher um parecer sobre a solicitação acadêmica do aluno

### Requisitos não Funcionais

* O software deve ser responsivo, para se adaptar a diferentes tipos de tela
* O software deverá ser de fácil entendimento e utilização, visando usuários com pouca habilidade em informática.
* O software deverá coletar métricas de uso para que possam ser usados em insights para melhor a experiência do usário
* 
* O software deve ter um sistema de autenticação seguro

## Projeto com visão de produto

### Análise de custo do projeto

|Profissional|Tipo da Empresa|Valor/Hora|Tempo De Desenvolvimento|Total
|----|------|------|--------|------|
|Engenheiro de Software Júnior|Grande Porte|R$33,00|3 Semanas(25 horas)|R$2475

## Arquitetura (v0.1)

* Padrão Arquitetural
  * MVT - Padrão Arquitetural usado pelo framework Django
  
  ![](https://mdn.mozillademos.org/files/13931/basic-django.png)

* MER

  ![](https://i.imgur.com/rotiFsL.jpg)
