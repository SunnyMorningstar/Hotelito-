# R1 gg JUJ
# R2 gg JUJ
# R3 gg? SNN
# R4 tem que ver certin como funfa SNN
# R5 gg? JUJ
# R6 gg JUJ
# R7 gg JUJ 
# R8 eu fiz mas tu tem que ver ainda JUJ
# R9 gg JUJ
#R10 nah



from abc import ABC, abstractmethod
from typing import Protocol

# O 3 tá subindo insta JUJ
# (interface)
# Qualquer classe que tenha o método descrever() "serve" como Descritivel,
# mesmo sem herdar daqui. Quarto e Hospede não têm herança em comum.

class Descritivel(Protocol):
    """Contrato: quem tem descrever() devolve um texto."""

    def descrever(self) -> str:
        ...






# não dá para criar Quarto() direto, CARAI JUJ
# só as filhas (Standard e Luxo). Ela define o "contrato" é simplim SNN

class Quarto(ABC):
    """Base de todos os quartos."""

    total_criados = 0  # R6 - atributo de CLASSE (um contador para todos) SNN

    def __init__(self, numero: int) -> None:  #  classe com __init__ e self SNN
        self.numero = numero      # chama o setter lá embaixo SNN
        self._ocupado = False     # "não mexa direto, use os métodos" JUJ

        Quarto.total_criados += 1


    # nuemros dos quartos é meio fake que pode por qualquer tralha
    @property
    def numero(self) -> int:
        """Número do quarto."""
        return self._numero

    @numero.setter
    def numero(self, valor: int) -> None:
        if valor > 0:             # só aceita número positivo SNN
            self._numero = valor


    # não guarda nada, calcula na hora)  SNN
    @property
    def disponivel(self) -> bool:
        """True se o quarto está livre."""
        return not self._ocupado

    def ocupar(self) -> None:
        """Marca o quarto como ocupado."""
        self._ocupado = True

    def liberar(self) -> None:
        """Marca o quarto como livre."""
        self._ocupado = False

    #  não usa self nem cls, é só uma ferramenta JUJ
    @staticmethod
    def formatar_dinheiro(valor: float) -> str:
        """Transforma 150 em 'R$ 150.00'."""
        return f"R$ {valor:.2f}"

    # cada filha é obrigada a escrever o seu mas é fake denovo kksk SNN

    @abstractmethod
    def calcular_diaria(self) -> float:
        """Valor de uma diária."""

    def descrever(self) -> str:
        """Texto do quarto (usa o calcular_diaria de cada filha)."""
        status = "Livre" if self.disponivel else "Ocupado"
        return (f"🛏️  Quarto {self.numero} - {self.formatar_dinheiro(self.calcular_diaria())}"
                f"/dia - {status}")








# Herança: QuartoStandard "é um" Quarto (e QuartoLuxo também) SNN
# calculo de diaria é com QuartoStandard e QuartoLuxo, lá no fundo é só um x=120 e y=300 SNN

class QuartoStandard(Quarto):
    """Quarto simples."""

    DIARIA_BASE = 150.0  # preço do quarto standard SNN

    def calcular_diaria(self) -> float:  
        return self.DIARIA_BASE


class QuartoLuxo(Quarto):
    """Quarto luxo: diária base + 10%."""


    DIARIA_BASE = 300.0
    TAXA = 0.10

    def calcular_diaria(self) -> float:  # as formula do paranaué SNN
        return self.DIARIA_BASE * (1 + self.TAXA)

    def descrever(self) -> str:  # aqui tá o Super() que ele pediu JUJ
        # super() chama o descrever() da classe Quarto (pai) e a gente acrescenta algo JUJ
        return super().descrever() + " (café da manhã incluso)"










# Hóspede (cliente do hotel)
# Eu não fiz nenhum verificador de CPF, nem nome, nem nada. se tu quiser fazer fé SNN

class Hospede:
    """Cliente do hotel."""

    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self._cpf = cpf  # R3 - protegido: só leitura pela property abaixo SNN

    @property
    def cpf(self) -> str:
        """CPF (só leitura, não tem setter)."""
        return self._cpf

    # construtor alternativo (recebe cls) SNN
    # GE SUS que isso é um método de classe, não de instância. Ele cria um objeto a partir de uma string JUJ
    @classmethod
    def from_string(cls, texto: str) -> "Hospede":
        """Cria hóspede a partir de 'nome;cpf'."""
        nome, cpf = texto.split(";")
        return cls(nome.strip(), cpf.strip())

    def descrever(self) -> str:
        """Texto do hóspede."""
        return f"🧳 Hóspede {self.nome} (CPF: {self.cpf})"

# a Reserva TEM um Hospede e TEM um Quarto dentro dela SNN
# "a Reserva TEM um Hospede e TEM um Quarto dentro dela" Burro 2026

class Reserva:
    """Liga um hóspede a um quarto por algumas diárias."""

    def __init__(self, hospede: Hospede, quarto: Quarto, diarias: int) -> None:
        self.hospede = hospede
        self.quarto = quarto
        self.diarias = diarias
        self.ativa = True

    def calcular_valor(self) -> float:
        """Diárias x valor da diária (cada tipo de quarto calcula diferente!)."""
        return self.diarias * self.quarto.calcular_diaria()

    def encerrar(self) -> None:
        """Check-out: libera o quarto."""
        self.ativa = False
        self.quarto.liberar()



# Hotel: guarda tudo e tem as REGRAS DE NEGÓCIO (o menu só chama estes métodos) SNN

class Hotel:
    """O hotel: quartos, hóspedes e reservas."""

    # tipos de quarto disponíveis no menu. Para criar um tipo novo: SNN
    # faça a subclasse e coloque aqui QUE EU N TANKO. SNN
    TIPOS = {"1": QuartoStandard, "2": QuartoLuxo}  # R6

    def __init__(self, nome: str) -> None:
        self.nome = nome
        # o Hotel guarda listas de outros objetos
        self._quartos: list[Quarto] = []
        self._hospedes: list[Hospede] = []
        self.__reservas: list[Reserva] = []  # "privado" (duplo underline) porque só o Hotel mexe com reservas JUJ




#AS DEF INFINITAS KKSKKKSKKS SNN
#its my way or the highway bitch JUJ


    @property
    def quartos(self) -> list[Quarto]:
        """Lista de quartos."""
        return self._quartos

    @property
    def hospedes(self) -> list[Hospede]:
        """Lista de hóspedes."""
        return self._hospedes

    def cadastrar_hospede(self, hospede: Hospede) -> None:
        """Guarda um hóspede."""
        self._hospedes.append(hospede)

    def cadastrar_quarto(self, tipo: str, numero: int) -> None:
        """Cria um quarto do tipo escolhido ('1' standard, '2' luxo)."""
        self._quartos.append(self.TIPOS[tipo](numero))


    def buscar_hospede(self, cpf: str):
        """Busca por CPF. Devolve o Hospede (ou None se não achar)."""
        for h in self._hospedes:
            if h.cpf == cpf:
                return h

    def buscar_quarto(self, numero: int):
        """Busca por número. Devolve o Quarto (ou None se não achar)."""
        for q in self._quartos:
            if q.numero == numero:
                return q

    # liga Hospede + Quarto JUJ
    def reservar(self, cpf: str, numero: int, diarias: int):
        """Cria a reserva se o quarto estiver livre. Devolve a Reserva (ou None)."""
        hospede = self.buscar_hospede(cpf)
        quarto = self.buscar_quarto(numero)
        if hospede and quarto and quarto.disponivel:
            quarto.ocupar()

            reserva = Reserva(hospede, quarto, diarias)
            self.__reservas.append(reserva)
            return reserva

    # aqui pra encerra a reserva JUJ
    def fazer_checkout(self, numero: int):
        """Faz o check-out do quarto. Devolve a Reserva (ou None)."""
        for r in self.__reservas:
            if r.ativa and r.quarto.numero == numero:
                r.encerrar()
                return r

    # - relatório de ocupação e faturamento JUJ
    def relatorio(self) -> str:
        """Ocupação e faturamento."""
        ocupados = sum(1 for q in self._quartos if not q.disponivel)
        faturado = sum(r.calcular_valor() for r in self.__reservas if not r.ativa)
        return (f"Quartos ocupados: {ocupados}/{len(self._quartos)}\n"
                f"Faturamento (check-outs feitos): {Quarto.formatar_dinheiro(faturado)}")


# MENU: só pergunta, chama o Hotel e mostra. Sem regra de negócio. simplim JUJ
# O 3 TÁ ERRADO JUJ 

#interface do usuário (menu) SNN logo a baixo:

def menu(Hotelito: Hotel) -> None:
    """Loop principal."""
    while True:
        print("\n===== HOTELITO =====")
        print("1 - Cadastrar hóspede\n2 - Cadastrar quarto\n3 - Listar quartos e hóspedes\n"
              "4 - Buscar hóspede por CPF\n5 - Fazer reserva\n6 - Fazer check-out\n"
              "7 - Relatório\n0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            Hotelito.cadastrar_hospede(Hospede(input("Nome: "), input("CPF: ")))
            print("✅ Hóspede cadastrado.")
        elif opcao == "2":
            tipo = input("Tipo (1 = Standard, 2 = Luxo): ")
            Hotelito.cadastrar_quarto(tipo, int(input("Número: ")))
            print("✅ Quarto cadastrado.")
        elif opcao == "3":



            # polimorvismo: lista mista, chamada igual para todos JUJ
            # n sei faze SNN



            itens: list[Descritivel] = [*Hotelito.quartos, *Hotelito.hospedes]
            for item in itens:
                print(item.descrever())
        elif opcao == "4":
            h = Hotelito.buscar_hospede(input("CPF: "))
            print(h.descrever() if h else "❌ Não encontrado.")
        elif opcao == "5":
            r = Hotelito.reservar(input("CPF: "), int(input("Quarto: ")), int(input("Diárias: ")))
            print(f"✅ Reservado! Total: {Quarto.formatar_dinheiro(r.calcular_valor())}"
                  if r else "❌ Não foi possível reservar.")
        elif opcao == "6":
            r = Hotelito.fazer_checkout(int(input("Quarto: ")))
            print(f"✅ Check-out de {r.hospede.nome}. Total: "
                  f"{Quarto.formatar_dinheiro(r.calcular_valor())}"
                  if r else "❌ Esse quarto não tem reserva.")
        elif opcao == "7":
            print(Hotelito.relatorio())
        elif opcao == "0":
            print("Até logo!")
            break




#os nossos hospedes presetados JUJ
def main() -> None:
    """Cria o hotelito com dados de exemplo e abre o menu."""
    hotelito = Hotel("Hotelito")
    hotelito.cadastrar_quarto("1", 101)
    hotelito.cadastrar_quarto("2", 201)

    hotelito.cadastrar_hospede(Hospede.from_string("Maria Silva;12345678901"))  # R4
    hotelito.cadastrar_hospede(Hospede("João Souza", "10987654321"))
    menu(hotelito)


if __name__ == "__main__":
    main()
