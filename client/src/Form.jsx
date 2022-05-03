import {
  Button, Container, NativeSelect, Space, TextInput, Title
} from '@mantine/core'
import { useForm } from '@mantine/form'
import React from 'react'
export function Form() {
  const datasetList = [
    'a280',
    'att48',
    'att532',
    'bays29',
    'berlin52',
    'burma14',
    'ch150',
    'eli176',
    'fri26',
    'gr120',
    'usa1359',
    'swiss42'
  ]
  const form = useForm({
    initialValues: {
      dataset: '',
      numCities: '',
    },
  });


  const handleSubmit = (values) => {
    let req;
    if(values.numCities === ""){
      req = {
        type : "DATASET",
        value : values.dataset
      }
    }else {
      req = {
        type : "VALUE",
        value : values.numCities
      }
    }
    console.log(req)
  // const res = await axios.post('/solve', req);
  // console.log(res.data)
  }

  return (
    <Container size={1000} my={40}>
      <Title order={5}> You can either choose to run the algorithm on an existing dataset or using a randomly generated dataset.</Title>
      <Space h="md"/>
      <form onSubmit={form.onSubmit(handleSubmit)}>
          <NativeSelect
                  data={datasetList}
                  placeholder="Pick one"
                  label="Choose the dataset"
                  radius="xs"
                  size="md"
                  {...form.getInputProps('dataset')}
            />
          <Space h='sm'/>
          <TextInput label="Number of cities to be generated" placeholder="Number of cities" type='number' {...form.getInputProps('numCities')} />

          <Button fullWidth mt="xl" type='submit'>
            Submit
          </Button>
      </form>

    </Container>
  );
}