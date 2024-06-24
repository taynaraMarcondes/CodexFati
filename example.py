example = [
  '''
  start
    theKnight op justice 1
    temperance value justice 0.0
    sun("digite um numero real:")
    moon(value)
    emperor(op != 0){
        sun("qual opcao deseja:")
        sun("0 - sair")
        sun("1 - somar 5.50")
        sun("2 - subtrair 3.50")
        moon(op)
        magician(op == 1) {
            value justice value + 5.5
            sun(value)
        } wheelOfFortune {
            magician(op == 2){
                value justice value - 3.5
                sun(value)
            } wheelOfFortune {
                sun("Opcao invalida")
            }
        }
    }
  end
  ''',
  '''
  start
    theKnight op justice 1
    temperance value justice 0.0
    sun("digite um numero real:")
    moon(value)
    emperor(op != 0){
        sun("qual opcao deseja:")
        sun("0 - sair")
        sun("1 - somar 5.50")
        sun("2 - subtrair 3.50")
        moon(op)
        magician(op == 1) {
            value justice value + 5.5
            sun(value)
        } wheelOfFortune {
            magician(op == 2){
                value justice value - 3.5
                sun(value)
            } wheelOfFortune {
                sun("Opcao invalida")
            }
        }
    }
  end
  ''',
  '''
  start
    theKnight op justice 1
    temperance value justice 0.0
    sun("digite um numero real:")
    moon(value)
    emperor(op != 0){
        sun("qual opcao deseja:")
        sun("0 - sair")
        sun("1 - somar 5.50")
        sun("2 - subtrair 3.50")
        moon(op)
        magician(op == 1) {
            value justice value + 5.5
            sun(value)
        } wheelOfFortune {
            magician(op == 2){
                value justice value - 3.5
                sun(value)
            } wheelOfFortune {
                sun("Opcao invalida")
            }
        }
    }
  end
  '''
]