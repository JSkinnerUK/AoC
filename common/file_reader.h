#ifndef FILE_READER_H
#define FILE_READER_H

// Type definition for the function pointer to handle lines
typedef void (*LineHandler)(const char *);

// Function prototype for read_file_lines
void read_file_lines(const char *fileName, LineHandler handler);

#endif // FILE_READER_H