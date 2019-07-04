
echo $0
echo $1

echo 192.168.3.2から$1.mp4をgetします。
python3 getMp4.py $1
if [ $? -ne 0 ]; then
	echo エラーが発生しました
else
	echo oto/に入っている*.mp4を全てmp3にコンバートして、oto2/に入れます。
	echo すでにコンバート済で、oto2/に存在するファイルは、コンバートしません。
	python3 mp4tomp3.py oto oto2
	 if [ $? -ne 0 ]; then
	 	echo エラーが発生しました。
	else
		rm oto/$1.mp4
		echo 完了しました。
	fi
fi


