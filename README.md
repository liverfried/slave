## File
```main.py``` è il programma che rimane sempre in esecuzione, esegue un ciclo scarica-esegui ogni 30 secondi

Link permanente (da aggiornare in caso di modifica): https://raw.githubusercontent.com/liverfried/slave/9ca2015b6be440efd2fdaf079443112e3a07928f/main.py

```payload.py``` è il programma scaricato ed eseguito

Il link https://raw.githubusercontent.com/liverfried/slave/main/payload.py ci mette un po' ad aggiornarsi dopo la modifica del file, e probabilmente rimane accessibile solo per un tempo limitato, ma per riattivarlo basta aprire il file dal sito in modalità raw

## Test eseguiti
- [x] Scaricare payload.py ed eseguirlo con ```exec()```
- [x] Utilizzare ```sleep()``` in ```exec()``` interrompe il ciclo scarica-esegui, quindi si possono sincronizzare i payload senza il rischio che se ne avii più di uno

- [x] Utilizzare ```os.remove(__file__)``` rimuove il programme
- [x] Utilizzare ```exit()``` nel payload termina il programma
- I due comandi precedenti insieme rimuovono ogni traccia del codice