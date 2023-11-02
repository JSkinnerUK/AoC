#ifndef FILE_READER_H
#define FILE_READER_H

typedef void (*LineHandler)(const char*);

void read_file_lines(const char* filename, LineHandler handler);

#endif // FILE_READER_H