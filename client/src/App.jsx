import {
  Container, createStyles, Paper, Title
} from '@mantine/core'
import React from 'react'
import { Form } from './Form'

const useStyles = createStyles((theme) => ({
  inner: {
    display: 'flex',
    justifyContent: 'space-between',
    paddingTop: theme.spacing.xl * 4,
    paddingBottom: theme.spacing.xl * 4,
  },

  content: {
    marginRight: theme.spacing.xl * 3,

    [theme.fn.smallerThan('md')]: {
      maxWidth: '100%',
      marginRight: 0,
    },
  },

  title: {
    textAlign : 'center',
    color: theme.colorScheme === 'dark' ? theme.white : theme.black,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    fontSize: 44,
    lineHeight: 1.2,
    fontWeight: 900,

    [theme.fn.smallerThan('xs')]: {
      fontSize: 28,
    },
  },

  control: {
    [theme.fn.smallerThan('xs')]: {
      flex: 1,
    },
  }
}));

function App() {
  const { classes } = useStyles();
  return (
    <div className='app'>
      <Container size='xl'>
      <Paper withBorder shadow="md" p={30} radius="xs">
        <div className={classes.inner}>
            <div className={classes.content}>
              <Title className={classes.title}>
                Traveling Salesperson problem using Genetic Algorithms
              </Title>
             </div>
          </div>
      </Paper>
      </Container>
      <Form/>
    </div>
  );
}

export default App;