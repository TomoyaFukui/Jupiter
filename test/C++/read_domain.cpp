#include <read_domain.h>
#include <fstream>

using namespace std;

class ReadDomain{
  void CopyFile( const char *from_file_name, const char *to_file_name )
  {
      ifstream is( from_file_name, ios::in | ios::binary );
      ofstream os( to_file_name, ios::out | ios::binary );

      // バッファ確保
      vector<char> buffer( 1024*1024 );
      // ファイルコピー
      while( !is.eof() )
      {
          size_t size = is.read( &buffer[0], buffer.size() ).gcount();
          os.write( &buffer[0], size );
      }
  }


}
