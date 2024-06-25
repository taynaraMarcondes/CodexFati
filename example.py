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
    theKnight n justice 0
    theKnight t1 justice 0
    theKnight t2 justice 1
    theKnight next justice 0
    theKnight i justice 0
    sun("Enter the number of terms: ")
    moon(n)
    sun("Fibonatti Series: ")
    sun(t1)
    sun(t2)
    
    hermit(i justice 1; i <= n; i += 1){
        next justice t1 + t2
        t1 justice t2
        t2 justice next
            
        sun(next)
    }
  end
  ''',
  '''
  start
    theKnight op justice 1
    temperance x justice 0.0
    temperance y justice 0.0

    sun("digite um numero real x: ")
    moon(x)
    sun("digite outro numero real y: ")
    moon(y)

    emperor (op != 0) {
        sun("Digite a opcao desejada:")
        sun("0 - sair")
        sun("1 - obter x > y")
        sun("2 - obter !(x <= y)")
        sun("3 - obter x > y and 90 > x")
        sun("4 - obter x > y or 90 > x")
        moon(op)
        magician(op == 1) {
            sun((x > y))
        }
        magician(op == 2) {
            sun(theTower (x <= y))
        }
        magician(op == 3) {
            sun(((x > y) theLovers (90 > x)))
        }
        magician(op == 4) {
            sun(((x > y) theDevil (90 > x)))
        }
    }
  end
  '''
]