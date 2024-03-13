#include <iostream>
#include <cctype>
#include <string>

using namespace std;

string polyalphabets_cipher(const string &cipher_text, int key)
{
    string result = "";

    for (char ch : cipher_text)
    {
        if (isalpha(ch))
        {
            char base = (isupper(ch)) ? 'A' : 'a';
            result += static_cast<char>((ch - base - key + 26) % 26 + base);
        }
        else
        {
            result += ch;
        }
    }

    return result;
}

int main()
{
    string cipher_text = "XTKG XTKMA LNKOXR LEBF";

    for (int i = 0; i < 26; ++i)
    {
        // Output the decrypted text for each possible key
        string possible_answer = polyalphabets_cipher(cipher_text, i);
        cout << possible_answer << ". Key: " << i + 1 << endl;
    }

    return 0;
}