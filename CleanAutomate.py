#Automação de Limpeza de Backups
"""BrainStorm:

Caminho das Pastas: \\10.1.2.35\backup\clientes\2023\1\ARH\C_AGUACLARA

 ==3 arquivos por mes nos anos de 2020 a 2022
 ==1 arquivo por dia nos anos de 2023 a 2024

 Entrar na pasta (Filho), fazer o processo. Ao Finalizar, retornar para pasta anterior(Pai) e acessar a pasta seguinte(Filho2).
 
 Validações: Verificar se à dois arquivos com mesmo nome 
 - verificar data do arquivo duplicado mantendo apenas um banco por dia
 - verificar qual tem o horario mais perto do fim do dia 
 - verificar tamanho do arquivo priorizando sempre o maior
 - Priorizar arquivo que possui SW no nome se passar pelas validações anteriores (Data/horario e tamanho)
 - na verificação de tamanho do arquivo, fazer média de todos os arquivos, os arquivos que tiver metade do tamanho da media dos arquivos devem ser deletados
 - no caso dos arquivos serem absolutamente iguais excluir duplicatas e manter apenas 1 arquivo
 
 - Testar a automação inserindo a letra "Z" no começo ou final do nome do arquivo
 - No caso de funcionar apenas trocar a função para que exclua os arquivos

 ----------------------------------------------------------------------------------
automação teste para adicionar "Z" dentro do nome dos backups e outra para retirar oq foi inserido.
 ----------------------------------------------------------------------------------
 - possibilidade de criar uma automação de inserção de caracteres predefinidos nos arquivos
   e outra automação apenas para validar e excluir arquivos com os caracteres."""