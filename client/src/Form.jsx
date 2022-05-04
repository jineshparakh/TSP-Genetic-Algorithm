import {
  Button, Container, Grid, LoadingOverlay, NativeSelect, NumberInput, Space, TextInput, Title
} from '@mantine/core'
import { useForm } from '@mantine/form'
import axios from 'axios'
import React, { useEffect, useState } from 'react'
import Modal from './Modal'

export function Form() {

  const [visible, setVisible] = useState(false);
  const [response, setResponse] = useState({})
  const [opened, setOpened] = useState(false);
  useEffect(() => {
    if(opened === false){
      setResponse({})
    }
  }, [opened])



  const datasetList = ['rd100', 'pcb442', 'pr2392', 'kroD100', 'd493', 'fl417', 'p654', 'u159', 'rl5915', 'nrw1379', 'fl1577', 'pr76', 'fl3795', 'u1432', 'kroA150', 'eil51', 'pr299', 'ts225', 'pr439', 'kroA100', 'u1817', 'kroB150', 'lin318', 'pr1002', 'brd14051', 'eil101', 'bier127', 'gil262', 'pr124', 'd18512', 'pcb1173', 'u2319', 'rat575', 'd1655', 'rl5934', 'u2152', 'u724', 'tsp225', 'rat783', 'fnl4461', 'vm1084', 'rd400', 'd657', 'u1060', 'rat195', 'ch150', 'pr152', 'usa13509', 'rl1304', 'berlin52', 'rl1323', 'jp', 'linhp318', 'kroB100', 'fl1400', 'pr144', 'u574', 'pr136', 'pcb3038', 'pr264', 'kroE100', 'rat99', 'd1291', 'pr107', 'kroA200', 'vm1748', 'd2103', 'st70', 'd198', 'ch130', 'pr226', 'rl11849', 'eil76', 'rl1889', 'a280', 'kroB200', 'kroC100', 'd15112', 'lin105']

  const form = useForm({
    initialValues: {
      dataset: '',
      numCities: '',
      popSize : 10,
      numGen: 3,
    },
  });


  const handleSubmit = async (values) => {
    setVisible(true)
    let req;
    if(values.numCities === ""){
      req = {
        type : "DATASET",
        value : values.dataset,
        pop_size : values.popSize,
        n_generations :values.numGen
      }
    } else {
      req = {
        type : "VALUE",
        value : values.numCities,
        pop_size : values.popSize,
        n_generations :values.numGen
      }
    }
    console.log(req)
    let res;
    try {
      res = await axios.post('/findSolution', req);
      setTimeout(() => {
        setResponse(res.data);
        setOpened(true)
        setVisible(false)
      }, 500);
    } catch (error) {
      console.error(error)
    }


  }

  return (
    <>
      <Modal data={response} opened={opened} setOpened={setOpened} />
      <Container size={1000} my={40}>
        <Title order={5}> You can either choose to run the algorithm on an existing dataset or using a randomly generated dataset.</Title>
        <Space h="md"/>
        <div>
        <LoadingOverlay visible={visible}  />
          <form onSubmit={form.onSubmit(handleSubmit)}>
             <Grid>
                <Grid.Col span={6}>
                  <NumberInput
                    defaultValue={10}
                    label="Population Size"
                    required
                    hideControls
                    {...form.getInputProps('popSize')}
                  />
                </Grid.Col>
                <Grid.Col span={6}>
                  <NumberInput
                    defaultValue={3}
                    label="Number of generations"
                    required
                    hideControls
                    {...form.getInputProps('numGen')}
                  />
                </Grid.Col>
              </Grid>
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
        </div>

      </Container>
    </>
  );
}