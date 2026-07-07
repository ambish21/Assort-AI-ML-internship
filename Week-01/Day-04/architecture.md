# MongoDB Architecture

Organization
│
├── Project
│
├── Cluster
│
├── Database
│
├── Collection
│
└── Document

## Explanation

### Organization

Contains multiple projects.

### Project

Groups databases for one application.

### Cluster

The MongoDB server where databases live.

### Database

Stores collections.

### Collection

Stores related documents.

### Document

Stores actual information in BSON (JSON-like) format.

Example

Student Database
    ↓
Students Collection
    ↓
{
    "name":"Ahmed",
    "semester":6
}