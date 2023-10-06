def turno(d):
    if d == '1' or d == '2' or d == '3' or d == '4':
        return 'Manha'
    elif d == '5' or d == '6' or d == '7' or d == '8':
        return 'Tarde'
    elif d == '9' or d == '10' or d == '11':
        return 'Noite'
def marcar(espec,medico, dia,horario):
    confconsulta=[]
    if espec == '1':
        if medico =='1':
            confconsulta.append('Dra Ana')            
            confconsulta.append(drana[0][int(dia)])
            confconsulta.append(turno(horario))               
            if drana[int(horario)][int(dia)] != '' and drana[int(horario)][int(dia)] != 'Ocupado':                    
                confconsulta.append(drana[int(horario)][int(dia)])
                drana[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta Marcada')
                
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia == '1' or dia == '1' or dia == '3' or dia == '4' or dia == '5':
                if  horario == '9' or horario == '10' or horario == '11':
                    confconsulta.clear()                
            print(horarioconfirmados)
            print()
        elif medico =='2':
            confconsulta.append('Dr Mauro')            
            confconsulta.append(drmauro[0][int(dia)])
            confconsulta.append(turno(horario))                               
            if drmauro[int(horario)][int(dia)] != '' and drmauro[int(horario)][int(dia)] != 'Ocupado':                                    
                confconsulta.append(drmauro[int(horario)][int(dia)])
                drmauro[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta Marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia =='1' or dia == '3':                
                confconsulta.clear()
            elif dia =='2' and horario == '9' or horario =='10' or horario =='11':                                                    
                confconsulta.clear()
            elif dia == '4' and horario =='5' or horario == '6' or horario == '7' or horario =='8':                
                confconsulta.clear()
            print(horarioconfirmados)
            print()
        elif medico =='3':
            confconsulta.append('Dr Lucas')            
            confconsulta.append(drlucas[0][int(dia)])
            confconsulta.append(turno(horario))                          
            if drlucas[int(horario)][int(dia)] != '' and drlucas[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(drlucas[int(horario)][int(dia)])
                drlucas[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta Marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia =='0':
                confconsulta.clear()
            elif dia =='1' or dia =='2':
                if horario == '9' or horario == '10' or horario == '11':
                    confconsulta.clear()                               
            elif dia == '4':
                if horario =='1' or horario == '2' or horario == '3' or horario =='4':
                    confconsulta.clear()
            print(horarioconfirmados)
            print()
    elif espec =='2':
        if medico =='4':
            confconsulta.append('Dr Claudio')
            confconsulta.append(drclaudio[0][int(dia)])
            confconsulta.append(turno(horario))                              
            if drclaudio[int(horario)][int(dia)] != '' and drclaudio[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(drclaudio[int(horario)][int(dia)])
                drclaudio[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta Marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia =='3' or dia =='4':
                confconsulta.clear()
            elif dia =='0' and horario =='5' or horario =='6' or horario =='7' or horario =='8':            
                confconsulta.clear()                               
            elif dia == '1' and horario =='1' or horario == '2' or horario == '3' or horario =='4':
                confconsulta.clear()
            print(horarioconfirmados)
            print()
        if medico == '5':
            confconsulta.append('Dr Carla')
            confconsulta.append(dracarla[0][int(dia)])
            confconsulta.append(turno(horario))                              
            if dracarla[int(horario)][int(dia)] != '' and dracarla[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(dracarla[int(horario)][int(dia)])
                dracarla[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia =='2' or dia =='3':
                confconsulta.clear()
            elif dia =='4' and horario =='5' or horario =='6' or horario =='7' or horario =='8':            
                confconsulta.clear()                           
            print(horarioconfirmados)
            print()
        if medico == '6':
            confconsulta.append('Dr Rita')
            confconsulta.append(drarita[0][int(dia)])
            confconsulta.append(turno(horario))                              
            if drarita[int(horario)][int(dia)] != '' and drarita[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(drarita[int(horario)][int(dia)])
                drarita[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta Marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia =='0' or dia =='1':
                confconsulta.clear()
            elif  dia =='2' and horario == '1' or horario == '2' or horario =='3' or horario =='4':            
                confconsulta.clear()
            elif  dia =='4' and horario == '1' or horario == '2' or horario =='3' or horario =='4':
                confconsulta.clear()                           
            print(horarioconfirmados)
            print()
    elif espec =='3':
        if medico =='7':
            confconsulta.append('Dr Antonio')
            confconsulta.append(drantonio[0][int(dia)])
            confconsulta.append(turno(horario))                              
            if drantonio[int(horario)][int(dia)] != '' and drantonio[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(drantonio[int(horario)][int(dia)])
                drantonio[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta Marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia =='3':                
                confconsulta.clear()
            elif dia == '0' or dia == '1' or dia == '2':
                if horario == '9' or horario == '10' or horario == '11':                              
                    confconsulta.clear()                               
            elif dia == '4' and horario == '5' or horario == '6' or horario == '7' or horario == '8':                
                confconsulta.clear()
            print(horarioconfirmados)
            print()
        elif medico == '8':
            confconsulta.append('Dr Alice')
            confconsulta.append(dralice[0][int(dia)])
            confconsulta.append(turno(horario))                              
            if dralice[int(horario)][int(dia)] != '' and dralice[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(dralice[int(horario)][int(dia)])
                dralice[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia == '1' or dia == '3':
                confconsulta.clear()
            elif dia == '0' or dia== '2'or dia== '4':
                if horario == '1' or horario == '2' or horario == '3' or horario == '4':                              
                    confconsulta.clear()                           
            print(horarioconfirmados)
            print()
        elif medico == '9':
            confconsulta.append('Dra Elis')
            confconsulta.append(drarita[0][int(dia)])
            confconsulta.append(turno(horario))                                          
            if draelis[int(horario)][int(dia)] != '' and draelis[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(draelis[int(horario)][int(dia)])
                draelis[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia == '1' or dia == '2'or dia == '3':
                confconsulta.clear()                          
            print(horarioconfirmados)
            print()
        elif medico == '0':
            confconsulta.append('Dr Ruan')
            confconsulta.append(drruan[0][int(dia)])                
            confconsulta.append(turno(horario))              
            if drruan[int(horario)][int(dia)] != '' and drruan[int(horario)][int(dia)] != 'Ocupado':                                            
                confconsulta.append(drruan[int(horario)][int(dia)])
                drruan[int(horario)][int(dia)]='Ocupado'
                horarioconfirmados.append(confconsulta)
                print()
                print('Consulta marcada')
            else:
                print('Medico nao atende no horario escolhido/Horario Ocupado\nEscolha novos horarios')
                confconsulta.clear()
            if dia == '0' or dia == '2':
                confconsulta.clear()
            elif  dia == '2' or dia == '3' or dia == '4':
                if horario == '9' or horario == '10' or horario == '11':            
                    confconsulta.clear()                         
            print(horarioconfirmados)
            print()
            
def menuinicial(texto):
    print()
    print('-' * 60 )
    print(f' {texto}')
    print('-' * 60 )

def medicos(med):
    print('-' * 60 )    
    if med == '1':
        print('-'*26,'Dr Ana','-'*25)        
        for l in range(len(drana)):
            for c in range(len(drana[l])):
                print(f'[{drana[l][c]:^10}]',end='')
            print()
        print()        
    if med == '2':
        print('-'*26,'Dr Mauro','-'*25)        
        for l in range(len(drmauro)):
            for c in range(len(drmauro[l])):
                print(f'[{drmauro[l][c]:^10}]',end='')
            print()
    if med =='3':
        print('-'*26,'Dr Lucas','-'*25)        
        for l in range(len(drlucas)):
            for c in range(len(drlucas[l])):
                print(f'[{drlucas[l][c]:^10}]',end='')
            print()
    if med == '4':
        print('-'*26,'Dr Claudio','-'*25)        
        for l in range(len(drclaudio)):
            for c in range(len(drclaudio[l])):
                print(f'[{drclaudio[l][c]:^10}]',end='')
            print()    
    if med == '5':
        print('-'*26,'Dra Carla','-'*25)       
        for l in range(len(dracarla)):
            for c in range(len(dracarla[l])):
                print(f'[{dracarla[l][c]:^10}]',end='')
            print()
    if med == '6':
        print('-'*26,'Dra Rita','-'*25)        
        for l in range(len(drarita)):
            for c in range(len(drarita[l])):
                print(f'[{drarita[l][c]:^10}]',end='')
            print()
    if med == '7':
        print('-'*26,'Dr Antonio','-'*25)        
        for l in range(len(drantonio)):
            for c in range(len(drantonio[l])):
                print(f'[{drantonio[l][c]:^10}]',end='')
            print()
    if med == '8':
        print('-'*26,'Dra Alice','-'*25)        
        for l in range(len(dralice)):
            for c in range(len(dralice[l])):
                print(f'[{dralice[l][c]:^10}]',end='')
            print()
    if med == '9':
        print('-'*26,'Dra Elis','-'*25)       
        for l in range(len(draelis)):
            for c in range(len(draelis[l])):
                print(f'[{draelis[l][c]:^10}]',end='')
            print()
    if med == '0':
        print('-'*26,'Dr Ruan','-'*25)        
        for l in range(len(drruan)):
            for c in range(len(drruan[l])):
                print(f'[{drruan[l][c]:^10}]',end='')
            print()
    print(' ' * 60 )       
def especialidades(esp):
    print('-' * 53)
    oftalmologista=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'], ['MANHA', 'MANHA', 'MANHA', 'MANHA', 'MANHA'], ['TARDE', 'TARDE', 'TARDE', 'TARDE', 'TARDE'], ['NOITE', '-----', '-----', 'NOITE', 'NOITE']]
    cardiologista= [['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'], ['MANHA', 'MANHA', 'MANHA', 'MANHA', '-----'], ['TARDE', 'TARDE', 'TARDE', 'TARDE', 'TARDE'], ['NOITE', 'NOITE', 'NOITE', 'NOITE', 'NOITE']]
    pediatra=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'], ['MANHA', 'MANHA', 'MANHA', 'MANHA', '-----'], ['TARDE', 'TARDE', 'TARDE', 'TARDE', 'TARDE'], ['NOITE', 'NOITE', 'NOITE', 'NOITE', 'NOITE']]    
    if esp == '1':
        print('-'*22,'OFTAMOLOGISTAS','-'*22)
        for l in range(len(oftalmologista)):
            for c in range(len(oftalmologista[l])):
                print(f'[{oftalmologista[l][c]:^10}]',end='')
            print()
    elif esp == '2':
        print('-'*22,'CARDIOLOGISTAS','-'*22)
        for l in range(len(cardiologista)):
            for c in range(len(cardiologista[l])):
                print(f'[{cardiologista[l][c]:^10}]',end='')
            print()
    elif esp == '3':
        print('-'*24,'PEDIATRAS','-'*24)
        for l in range(len(pediatra)):
            for c in range(len(pediatra[l])):
                print(f'[{pediatra[l][c]:^10}]',end='')
            print()  
    print(' ' * 60)
def diadasemana(coluna,espec):
    print('-' * 60)    
    oftalmologista=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'], ['MANHA', 'MANHA', 'MANHA', 'MANHA', 'MANHA'], ['TARDE', 'TARDE', 'TARDE', 'TARDE', 'TARDE'], ['NOITE', '-----', '-----', 'NOITE', 'NOITE']]
    cardiologista= [['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'], ['MANHA', 'MANHA', 'MANHA', 'MANHA', '-----'], ['TARDE', 'TARDE', 'TARDE', 'TARDE', 'TARDE'], ['NOITE', 'NOITE', 'NOITE', 'NOITE', 'NOITE']]
    pediatra=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'], ['MANHA', 'MANHA', 'MANHA', 'MANHA', '-----'], ['TARDE', 'TARDE', 'TARDE', 'TARDE', 'TARDE'], ['NOITE', 'NOITE', 'NOITE', 'NOITE', 'NOITE']]
    if espec == '1':
        print('OFTMOLOGISTA - VEJA HORARIOS DISPONIVES')
        for i in range(len(oftalmologista)):
            print(f'[{oftalmologista[i][int(coluna)]:^10}]')
    elif espec == '2':
        print(' CARDIOLOGISTA - VEJA HORARIOS DISPONIVES')
        for i in range(len(cardiologista)):
            print(f'[{cardiologista[i][int(coluna)]:^10}]')
    elif espec == '3':
        print('PEDIATRA - VEJA HORARIOS DISPONIVES')
        for i in range(len(pediatra)):
            print(f'[{pediatra[i][int(coluna)]:^10}]')
    print(' ' * 60)
    

drana=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'], ['08:00', '08:00', '08:00', '08:00', '08:00'], ['09:00', '09:00', '09:00', '09:00', '09:00'], ['10:00', '10:00', '10:00', '10:00', '10:00'], ['11:00', '11:00', '11:00', '11:00', '11:00'], ['13:00', '13:00', '13:00', '13:00', '13:00'], ['14:00', '14:00', '14:00', '14:00', '14:00'], ['15:00', '15:00', '15:00', '15:00', '15:00'], ['16:00', '16:00', '16:00', '16:00', '16:00'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
drmauro=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['08:00', '', '08:00', '', '08:00'],['09:00', '', '09:00', '', '09:00'],['10:00', '', '10:00', '', '10:00'],['11:00', '', '11:00', '', '11:00'],['13:00', '', '13:00', '', ''],['14:00', '', '14:00', '', ''],['15:00', '', '15:00', '', ''],['16:00', '', '16:00', '', ''],['18:00', '', '', '', '18:00'],['19:00', '', '', '', '19:00'],['20:00', '', ' ', '', '20:00']]
drlucas=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['', '08:00', '08:00', '08:00', ''],['', '09:00', '09:00', '09:00', ''],['', '10:00', '10:00', '10:00', ''],['', '11:00', '11:00', '11:00', ''],['', '13:00', '13:00', '13:00', '13:00'],['', '14:00', '14:00', '14:00', '14:00'],['', '15:00', '15:00', '15:00', '15:00'],['', '16:00', '16:00', '16:00', '16:00'],['', '', '', '18:00', '18:00'],['', '', '', '19:00', '19:00'],['', '', '', '20:00', '20:00']]
drclaudio=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['08:00', '', '08:00', '', ''],['09:00', '', '09:00', '', ''],['10:00', '', '10:00', '', ''],['11:00', '', '11:00', '', ''],['', '13:00', '13:00', '', ''],['', '14:00', '14:00', '', ''],['', '15:00', '15:00', '', ''],['', '16:00', '16:00', '', ''],['18:00', '18:00', '', '', ''],['19:00', '19:00', '', '', ''],['20:00', '20:00', '', '', '']]
dracarla=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['08:00', '08:00', '', '', '08:00'],['09:00', '09:00', '', '', '09:00'],['10:00', '10:00', '', '', '10:00'],['11:00', '11:00', '', '', '11:00'],['13:00', '13:00', '', '', ''],['14:00', '14:00', '', '', ''],['15:00', '15:00', '', '', ''],['16:00', '16:00', '', '', ''],['18:00', '18:00', '', '', '18:00'],['19:00', '19:00', '', '', '19:00'],['20:00', '20:00', '', '', '20:00']]
drarita=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['', '', '', '08:00', ''],['', '', '', '09:00', ''],['', '', '', '10:00', ''],['', '', '', '11:00', ''],['', '', '13:00', '13:00', '13:00'],['', '', '14:00', '14:00', '14:00'],['', '', '15:00', '15:00', '15:00'],['', '', '16:00', '16:00', '16:00'],['', '', '18:00', '18:00', '18:00'],['', '', '19:00', '19:00', '19:00'],['', '', '20:00', '20:00', '20:00']]
drantonio=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['08:00', '08:00', '08:00', '', '08:00'],['09:00', '09:00', '09:00', '', '09:00'],['10:00', '10:00', '10:00', '', '10:00'],['11:00', '11:00', '11:00', '', '11:00'],['13:00', '13:00', '13:00', '', ''],['14:00', '14:00', '14:00', '', ''],['15:00', '15:00', '15:00', '', ''],['16:00', '16:00', '16:00', '', ''],['', '', '', '', '18:00'],['', '', '', '', '19:00'],['', '', '', '', '20:00']]
dralice=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['', '', '', '', ''],['', '', '', '', ''],['', '', '', '', ''],['', '', '', '', ''],['13:00', '', '13:00', '', '13:00'],['14:00', '', '14:00', '', '14:00'],['15:00', '', '15:00', '', '15:00'],['16:00', '', '16:00', '', '16:00'],['18:00', '', '18:00', '', '18:00'],['19:00', '', '19:00', '', '19:00'],['20:00', '', '20:00', '', '20:00']]
draelis=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['08:00', '', '', '', '08:00'],['09:00', '', '', '', '09:00'],['10:00', '', '', '', '10:00'],['11:00', '', '', '', '11:00'],['13:00', '', '', '', '13:00'],['14:00', '', '', '', '14:00'],['15:00', '', '', '', '15:00'],['16:00', '', '', '', '16:00'],['18:00', '', '', '', '18:00'],['19:00', '', '', '', '19:00'],['20:00', '', '', '', '20:00']]
drruan=[['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA'],['', '08:00', '', '08:00', '08:00'],['', '09:00', '', '09:00', '09:00'],['', '10:00', '', '10:00', '10:00'],['', '11:00', '', '11:00', '11:00'],['', '13:00', '', '13:00', '13:00'],['', '14:00', '', '14:00', '14:00'],['', '15:00', '', '15:00', '15:00'],['', '16:00', '', '16:00', '16:00'],['', '', '', '', ''],['', '', '', '', ''],['', '', '', '', '']]
confconsulta=[]
horarioconfirmados=[]
seguir ='A'

while seguir !='B':    
    n='O que deseja faser?\n [1] - ESCOLHA UM MEDICO PARA VER HORAIOS: \n [2] - ESCOLHA UMA ESPECIALIDADE PARA VER HORARIOS DISPONIVEIS: \n [3] - ESCOLHA DIA DA SEMANA E ESPECIALIDADE PARA SABER HORARIOS DISPONIVEIS: \n [4] - AGENDAR HORARIO\n [5] - SAIR'

    menuinicial(n)
    botao=(input('Digite um numero: ')).upper()    
    if botao == '1':
        opcao='n'
        while  opcao != 'S':
            opcao=input('Medicos disponiveis:\n ---OFTALMOLOGISTA---\n [1]-Dra Ana\n [2]-Dr Mauro\n [3]-Dr Lucas\n ---CARDIOLOGISTA---\n [4]-Dr Claudio\n [5]-Dra Carla\n [6]-Dra Rita\n ----PEDIATRA----\n [7]-Dr Antonio\n [8]-Dra Alice\n [9]-Dra Elis\n [0]-Dr Ruan\n Digite o numer do medico ou S para sair: ').upper()
            medicos(opcao)
    elif botao == '2':
        opcao='n'
        while  opcao != 'S':
            opcao=input('Escolha a especialidade:\n [1] - Ofitalmologia\n [2] - Cardiologia\n [3] - Pediatria\n Digite uma especialidade para ver horarios ou S para sair: ').upper()
            especialidades(opcao)
    elif botao == '3':
        opcao='n'
        while  opcao != 'S':
            print('Escolha o dia da semana:\n [0] - Segunda\n [1] - Terca\n [2] - Quarta\n [3] - Quinta\n [4] - Sexta')
            opcao=(input('Escolha dia da semana ou S para sair: ')).upper()
            if opcao != 'S':
                especialida=input('Escolha a especialidade:\n [1] - Ofitalmologia\n [2] - Cardiologia\n [3] - Pediatria\n Digite uma especialidade para ver horarios ou S para sair: ').upper()
                if  especialida != 'S':
                    diadasemana(opcao,especialida)
                else:
                    opcao='S'
    elif botao == '4':
        opcao='N'
        while  opcao != 'S':            
            espec=input('Qual especialidade deseja atendimento?\n [1]- Oftalmologista\n [2]- Cardiologista\n [3]- Pediatra\n Digite o numero ou S para Sair:').upper()
            if espec != 'S':
                if espec == '1':
                    medico=input('Medicos disponiveis:\n ---OFTALMOLOGISTA---\n [1]-Dra Ana\n [2]-Dr Mauro\n [3]-Dr Lucas\n Digite o numero ou S para Sair: ').upper()
                elif espec =='2':
                    medico=input('Medicos disponiveis:\n ---CARDIOLOGISTA---\n [4]-Dr Claudio\n [5]-Dra Carla\n [6]-Dra Rita\n Digite o numero ou S para Sair: ').upper()
                elif espec =='3':
                    medico=input('Medicos disponiveis:\n ----PEDIATRA----\n [7]-Dr Antonio\n [8]-Dra Alice\n [9]-Dra Elis\n [0]-Dr Ruan\n Digite o numero ou S para Sair: ').upper()
                if medico !='S':                    
                    dia=input('Qual dia da semana deseja ser atendido?\n [0]- Segunda\n [1]- Terca\n [2]- Quarta\n [3]- Quinta\n [4]- Sexta\n Digite o numero ou S para Sair: ').upper()
                    if dia != 'S':
                        horario=input('Qual horario deseja atendimento?\n [1]-08:00\n [2]-09:00\n [3]-10:00\n [4]-11:00\n [5]-13:00\n [6]-14:00\n [7]-15:00\n [8]-16:00\n [9]-18:00\n [10]-19:00\n [11]-20:00\n Digite o numero ou S para Sair: ').upper()
                        if horario != 'S':
                            marcar(espec,medico,dia,horario)
                            turno(horario)
                        else:
                            opcao = 'S'
                    else:
                        opcao ='S'
                else:
                    opcao ='S'
            else:
                opcao ='S'    
    elif botao =='5':
        seguir= 'N'
        while seguir == 'N':
            botao = input('Deseja realmente Sair S/N: ').upper()
            if botao == 'N':
                seguir='S'                
            else:
                seguir = 'B'
                print('Obrigado e volte sempre')





