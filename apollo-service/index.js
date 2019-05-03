const { ApolloServer, gql } = require('apollo-server');
const { RESTDataSource } = require('apollo-datasource-rest');

class BooksAPI extends RESTDataSource {
    constructor() {
        super()
        this.baseURL = "http://localhost:5001/"
    }

    async getBook(id) {
        return this.get(`books/${id}`)
    }

    async getBooks(page = 1, limit = 10) {
        const response = await this.get('books', {})
        return response
    }
}

class AuthorsAPI extends RESTDataSource {
    constructor() {
        super()
        this.baseURL = "http://localhost:5000/"
    }

    async getAuthor(id) {
        return this.get(`authors/${id}`)
    }

    async getAuthors(page = 1, limit = 10) {
        const response = await this.get('authors', {})
        return response
    }
}

const typeDefs = gql`
  # Author
  type Author {
    id: ID!
    name: String
    about: String
  }

  type Book {
    id: ID!
    title: String
    pages: Int
    author: Author
  }

  type Query {
    book(id: ID!): Book
    books: [Book]
    author(id: ID!): Author
    authors: [Author]
  }
`;

const resolvers = {
  Query: {
    book: async (_source, { id }, { dataSources }) => {
        return dataSources.booksAPI.getBook(id)
    },
    books: async (_source, _args, { dataSources }) => {
        return dataSources.booksAPI.getBooks(1, 30)
    },
    author: async (_source, { id }, { dataSources }) => {
        return dataSources.authorsAPI.getAuthor(id)
    },
    authors: async (_source, { id }, { dataSources }) => {
        return dataSources.authorsAPI.getAuthors()
    }
  },
  Book: {
    author: async (parent, _args, { dataSources }) => {
        return dataSources.authorsAPI.getAuthor(parent.authorId)
    }
  }
};

const server = new ApolloServer({
    typeDefs,
    resolvers,
    dataSources: () => {
        return {
            booksAPI: new BooksAPI(),
            authorsAPI: new AuthorsAPI()
        }
    },
    context: () => {}
});

server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
