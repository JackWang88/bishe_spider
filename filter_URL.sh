grep "http://alexa.chinaz.com/?domain=" ./* >> ./legal_website_URL.txt
cat legal_website_URL.txt | cut -d ' ' -f 3 >> legal_website_URL_cut.txt
cat legal_website_URL_cut.txt  | cut -c 39- >> legal_website_URL_cut_cut.txt
cat legal_website_URL_cut_cut.txt | tr -d '"' >> legal_website_URL_tr.txt
cat legal_website_URL_tr.txt >> legal_website_URL.txt
