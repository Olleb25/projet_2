class ErreurDate(RuntimeError):
    def __str__(self):
        return "Date invalide!"

class ErreurQuantité(RuntimeError):
    def __str__(self):
        return "Quantité invalide!"
    
class LiquiditéInsuffisante(RuntimeError):
    def __str__(self):
        return "Liquidité insuffisante!"
    