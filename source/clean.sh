#!/bin/sh


cleanFile() {
	cd $1
	rm -rf *cache*
	rm -rf *.log
	cd -
}

scan1LevelDir(){
	for dirName in `ls`
	do
		if [ -d $dirName ]
		then
			cleanFile $dirName
		fi
	done
}

main(){
	scan1LevelDir
	cleanFile
}

main
