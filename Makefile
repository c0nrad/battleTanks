run:
	python2.7 battleTanks.py

clean:
	touch lol.lol~
	touch lol.pyc
	rm *~
	rm *.pyc 
	touch bots/lol.lol~
	touch bots/lol.pyc
	rm bots/*~
	rm bots/*.pyc
