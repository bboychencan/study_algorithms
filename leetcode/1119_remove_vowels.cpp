#include <string>
using namespace std;

string removeVowels(string S){
	string res = "";
	for(int i=0; i<S.size(); i++){
		if(S[i] != 'a' && S[i] != 'e' && S[i] != 'i' && S[i] != 'o' && S[i] != 'u'){
			res += S[i];
		}
	}
	return res;
}

int main(){
	
}